from django.shortcuts import render

def about_view(request):
    template_name = 'about/index.html'
    return render(request, template_name)
