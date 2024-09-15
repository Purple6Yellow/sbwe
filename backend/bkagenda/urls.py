from django.urls import path
from . import views

urlpatterns = [
    path('post_list.html/', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_inhoud'),
]