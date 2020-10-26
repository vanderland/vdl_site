from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import Contact
from .forms import ContactForm


class ContactIndex(generic.View):
    def get(self, request):
        template_name = 'contact/index.html'
        return render(request, template_name)


class ContactCreate(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('about:index')


class ContactRead(generic.ListView):
    model = Contact
    paginate_by = 2
    template_name = 'contact/read.html'
    context_object_name = 'contact_read'

    # def get_queryset(self):
    #     return Contact.objects.order_by('-created_on')[:50]


class ContactUpdate(generic.UpdateView):
    model = Contact    
    form_class = ContactForm
    template_name = 'contact/update.html'
    success_url = reverse_lazy('contact:read')


class ContactDelete(generic.DeleteView):
    model = Contact
    template_name = 'contact/delete.html'
    success_url = reverse_lazy('contact:read')

