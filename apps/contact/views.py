from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Contact
from .forms import ContactForm

class ContactList(generic.ListView):
    template_name = 'contact/list.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.order_by('-created_on')[:20]



class ContactCreate(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('contact:list')


class ContactUpdate(generic.UpdateView):
    model = Contact    
    form_class = ContactForm
    template_name = 'contact/update.html'
    success_url = reverse_lazy('contact:list')


class ContactDelete(generic.DeleteView):
    model = Contact
    template_name = 'contact/delete.html'
    success_url = reverse_lazy('contact:list')

