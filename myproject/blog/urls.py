from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('new_faker', views.new_faker, name="new_faker"),
]