from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_dash, name='home_dash'),
    path('add', views.add_device, name='add_device'),
    path('work/flow', views.work_flow, name='work_flow'),
    path('search/clients', views.search_clients, name='search_clients'),
    path('search/clients/<int:pk>', views.thin_uint, name='thin_uint'),

]
