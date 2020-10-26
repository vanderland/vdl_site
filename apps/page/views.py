from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import Page
from .forms import PageForm


# class PageIndex(generic.View):
#     def get(self, request):
#         template_name = 'page/index.html'
#         return render(request, template_name)


class PageDetail(generic.DetailView):
    model = Page
    template_name = 'page/detail.html'
    success_url = reverse_lazy('page:read')


class PageCreate(generic.CreateView):
    model = Page
    form_class = PageForm
    template_name = 'page/create.html'
    success_url = reverse_lazy('page:read')


class PageRead(generic.ListView):
    template_name = 'page/read.html'
    context_object_name = 'page_read'

    def get_queryset(self):
        return Page.objects.order_by('-created_on')[:50]


class PageUpdate(generic.UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'page/update.html'
    success_url = reverse_lazy('page:read')


class PageDelete(generic.DeleteView):
    model = Page
    template_name = 'page/delete.html'
    success_url = reverse_lazy('page:read')
