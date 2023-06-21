from django.urls import path
from dashboard_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.data_api, name='data_api'),
]
