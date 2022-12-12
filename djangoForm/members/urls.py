from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='index'),
    path('complain', views.complain, name='complain'),
    path('show', views.show, name='show'),
    # path('temp', views.contact, name='temp'),
    path('edit/<int:id>' , views.edit, name='edit'),
    path('update/<int:id>' , views.update, name='update'),
    path('delete/<int:id>' , views.delete, name='delete'),
]