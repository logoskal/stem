from django.db import models
from multiupload.fields import MultiImageField
from PIL import Image as PilImage
from io import BytesIO
from django.core.files import File

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Product Name')
    model = models.CharField(max_length=20, blank=False, null=True, verbose_name= 'Model')
    brand = models.CharField(max_length=20, blank=False, null=True, verbose_name='Brand (Manufacturer)')
    description = models.CharField(max_length=1000, verbose_name='Product Description')
    price = models.IntegerField(blank=True, null=True, verbose_name='General Price')
    category = models.ForeignKey(related_name='products',blank=True, null=True, to='Category', on_delete=models.DO_NOTHING, verbose_name='Category')
    quantity = models.IntegerField(blank=True, null=True, verbose_name='Available Number')
    weight = models.FloatField(blank=True, null=True, verbose_name='Product Weight (In K.G.)')
    status = models.BooleanField(default=True, blank=False, null=True, verbose_name='Availability')
    brochure = models.FileField(blank=True, null=True, verbose_name="Brochure PDF", upload_to='files/brochures/')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        if self.model != None and self.brand != None:
            return self.model + ' - ' + self.brand
        else:
            return self.name
        

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')
    description = models.CharField(max_length=1000, verbose_name='Category Description')
    image = models.ImageField(upload_to='images/category/thumbnails/', verbose_name='Category Image')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
         return self.name

class Image(models.Model):
    product = models.ForeignKey(to='Product', related_name='images' ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-images/')

    def __str__(self):
        return str(self.product.name + "'s Image - ") + str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image:
            img = PilImage.open(self.image.path)
            if True:#img.width > 500 and img.height > 500:
                output_size = (500,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.width > 500:
                output_size = (500, img.width)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height > 500:
                output_size = (img.height, 500)
                img.thumbnail(output_size)
                img.save(self.image.path)
