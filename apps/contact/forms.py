from django.forms import ModelForm
from .models import Contact
  
class ContactForm(ModelForm):

  class Meta:
          model = Contact
          # fields = ('name_first','name_middle','name_last','email_address','subject','message')
          fields = '__all__'

