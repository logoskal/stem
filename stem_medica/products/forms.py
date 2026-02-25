from django import forms
from .models import Product, Image, Category
from multiupload.fields import MultiFileField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ImageForm(forms.Form):
    image = MultiFileField(min_num=1, max_num=5, max_file_size= 1024 * 1024 * 5)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    # name = forms.CharField(max_length=50)
    # model = forms.CharField(max_length=20, blank=True)
    # brand = forms.CharField(max_length=20, blank=True)
    # description = forms.CharField(max_length=1000)
    # images = forms.ImageField()
    # price = forms.IntegerField(blank=True)
    # category = forms.
    # quantity = forms.IntegerField(blank=True)
    # weight = forms.FloatField(blank=True)
    # status = forms.BooleanField()
