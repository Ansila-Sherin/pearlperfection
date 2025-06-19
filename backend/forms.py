from django.forms import ModelForm
from backend.models import *

class ProductForm(ModelForm):
    class Meta:
        model=productTable
        fields="__all__"