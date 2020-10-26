from django.urls import path, re_path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.ContactIndex.as_view(), name='index'),
    path('create/', views.ContactCreate.as_view(), name='create'),
    path('read/', views.ContactRead.as_view(), name='read'),
    path('<int:pk>/update/', views.ContactUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ContactDelete.as_view(), name='delete'),
   
]
