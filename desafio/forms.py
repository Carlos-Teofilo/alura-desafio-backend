from django import forms

from desafio.models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['titulo', 'cor']

    cor = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color'}),
        label='Cor',
        max_length=7,
        initial='#000000'
    )