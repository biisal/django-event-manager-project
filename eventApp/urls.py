from django.urls import path
from . import views

urlpatterns = [
   path('create/', views.create, name="create"),
   path('view/', views.view, name="view"),
   path('edit/<int:id>/', views.edit, name="edit"),
   path('delete/<int:id>/', views.delete, name="delete"),
   path('view/details/<int:id>/', views.details, name="details"),
]


