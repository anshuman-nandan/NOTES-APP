from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('notespage/<str:pk>/', views.notespage, name='notes'),
    path('newnote/', views.newnote, name='newnote'),
    path('modifiednote/<str:pk>/', views.modifiednote, name='modifiednote'),
    path('deletenote/<str:pk>/', views.deletenote, name='delete'),
    path('bookmark/<str:pk>/', views.addBookmark, name="addBookmark"),
    path('deletebookmark/<str:pk>/', views.deleteBookmark, name="deleteBookmark"),
    path('viewbookmarks/', views.viewbookmarks, name="viewbookmarks")
]
