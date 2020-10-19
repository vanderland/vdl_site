from django.urls import path, re_path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.ContactCreate.as_view(), name='create'),
    path('list/', views.ContactList.as_view(), name='list'),
    path('<int:pk>/update/', views.ContactUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ContactDelete.as_view(), name='delete'),
   
]
