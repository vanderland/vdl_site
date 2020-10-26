from django.urls import path, re_path
from . import views

app_name = 'page'
urlpatterns = [
    path('create/', views.PageCreate.as_view(), name='create'),
    path('read/', views.PageRead.as_view(), name='read'),
    path('<slug:slug>', views.PageDetail.as_view(), name='detail'),
    path('<int:pk>/update/', views.PageUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.PageDelete.as_view(), name='delete'),

]
