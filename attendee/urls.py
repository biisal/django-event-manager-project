from django.urls import path
from . import views

urlpatterns = [
    path('allevents/', views.allevents, name="allevents"),
    path('register/<int:id>/', views.register, name="register"),
]


