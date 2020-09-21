from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('professors/<int:professor_id>/', views.professor, name='professor_page'),
]