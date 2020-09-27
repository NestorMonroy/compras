from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Categoria, SubCategoria


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


class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = [ 'categoria' ,'descripcion', 'estado']
        labels = { 'descripcion':'Descripcion de la  Sub Categoria',
                'estado':'Estado'}
        widgets={'descripcion': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args,*kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.update({
                    'class':'form-control'
                })
                
            self.fields['categoria'].empty_label = "Selecione Categoria"

