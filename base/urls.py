from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('notespage/<str:pk>/', views.notespage, name='notes'),
    path('newnote/', views.newnote, name='newnote'),
]
