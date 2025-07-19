from django import forms
from products.models import Car


class EditProduct(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['created_at', 'updated_at']  # exclude these fields

        