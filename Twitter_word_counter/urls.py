from django.urls import path

from . import views

urlpatterns = [
    path('', views.PageView),
    path('GetData/', views.GetData),
    path('DeleteData/', views.DeleteData),
]