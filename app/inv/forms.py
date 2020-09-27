from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Categoria, SubCategoria, Marca


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
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    
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


class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

