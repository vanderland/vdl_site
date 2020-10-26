from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact
  
class ContactForm(ModelForm):

  class Meta:
          model = Contact
          # fields = ('name_first','name_middle','name_last','email_address','subject','message')
          fields = '__all__'
          widgets = {
              'name_first': TextInput(attrs={'class': 'form-control'}),
              'name_middle': TextInput(attrs={'class': 'form-control'}),
              'name_last': TextInput(attrs={'class': 'form-control'}),
              'email_address': EmailInput(attrs={'class': 'form-control'}),
              'subject': TextInput(attrs={'class': 'form-control'}),
              'message': Textarea(attrs={'class': 'form-control'}),

          }
          # widgets = {
          #   'name_first': TextInput(attrs={'class': 'form-control'}),
          #   'message': Textarea(attrs={'class': 'form-control'}),
          # }
