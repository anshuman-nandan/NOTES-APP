from django.urls import path
from . import views


urlpatterns = [
    path('', views.notes, name="notes"),
    path('createnotes/',views.createnotes, name="createnotes"),
    path('readnotes/<str:pk>/', views.readnotes, name="readnotes"),
    path('updatenotes/<str:pk>/', views.updatenotes, name="updatenotes"),
    path('deletenotes/<str:pk>/', views.deletenotes, name="deletenotes"),
]