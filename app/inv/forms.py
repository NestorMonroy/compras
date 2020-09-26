from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = { 'descripcion':'Descripcion de la Categoria',
                'estado':'Estado'}
        widgets={'descripcion': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args,*kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.update({
                    'class':'form-control'
                })