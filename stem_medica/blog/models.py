from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=70, verbose_name='Blog Title', null=True)
    subtitle = models.CharField(max_length=121, verbose_name='Blog Sub-Title', null=True)
    bg_image = models.ImageField(upload_to='images/blog/blog-images', verbose_name='Title\'s Background Picture', null=True)
    date = models.DateTimeField(auto_now_add=True)
    intro = models.TextField(verbose_name='Introductory Text', blank=True, null=True)
    header_1 = models.CharField(max_length=70, verbose_name='Content Header 1', blank=True, null=True)
    content_1 = models.TextField(verbose_name="Content", blank=True, null=True)
    content_1_image = models.ImageField(upload_to='image/blog/blog-image', blank=True, null=True)
    header_2 = models.CharField(max_length=70, verbose_name='Content Header 2', null=True, blank=True)
    content_2 = models.TextField(verbose_name="Content", blank=True, null=True)
    content_2_image = models.ImageField(upload_to='image/blog/blog-image', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Blog " + str(self.id) + " " + self.title