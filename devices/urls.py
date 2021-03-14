from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_dash, name='home_dash'),
    path('add', views.add_device, name='add_device'),
    path('work/flow', views.work_flow, name='work_flow'),
    path('search/clients', views.search_clients, name='search_clients'),
    path('search/clients/<int:pk>', views.thin_uint, name='thin_uint'),
    path('reports/today', views.ClientsTodayReport.as_view(), name='report-today'),
    path('reports/store', views.ClientsAllReport.as_view(), name='report-store'),
    path('reports/unit', views.report, name='report-sara'),
    path('sara/grid', views.sara_grid, name='sara-grid'),
    path('delete/thin', views.delete_thin, name='delete_thin'),
    path('get/thin', views.get_thin_byId, name='get_thin'),
    path('update/thin', views.update_thin, name='update_thin'),
    path('create/thin', views.create_thin, name='create_thin'),

]
