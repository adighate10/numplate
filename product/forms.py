from django import forms
from django.forms import ModelForm
from .models import Photo
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        widgets ={
        	'name': forms.TextInput(attrs={'class': 'input100'}),
        	'image': forms.FileInput(attrs={'class': 'upload-btn-wrapper'}),
        }
        fields = ('name','image',)