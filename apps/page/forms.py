from django.forms import ModelForm, TextInput, CheckboxInput, Textarea
from .models import Page


class PageForm(ModelForm):

    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'}),

        }
