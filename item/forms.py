from django import forms

from .models import Item

class NewItemForm(forms.Form):
    class Meta:
        modle=Item
        fields = ('name', 'price', 'category', 'description', 'image')