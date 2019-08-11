from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('new/', views.new, name="upload"),
    path('create/', views.create, name="img_upload"),
    path('delete/<int:portfolio_id>/', views.delete, name="img_delete"),
]