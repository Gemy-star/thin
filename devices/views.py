from django.shortcuts import render, redirect
from . import models
from .filters import ThinClientFilter


def home_dash(request):
    return render(request, 'devices/home-dash.html')


def add_device(request):
    if request.method == "GET":
        return render(request, 'devices/add_device.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        total_devices = request.POST.get('total_devices')
        status = request.POST.get('status')
        epg = request.POST.get('epg')
        cdb = request.POST.get('cdb')
        db_zone = request.POST.get('database_zone')
        db_name = request.POST.get('database_name')
        short_name = request.POST.get('short_name')
        category = request.POST.get('category')
        client = models.ThinDevicesUnits(name=name, total_devices=total_devices, status=status, epg=epg, cdb=cdb,
                                         database_name=db_name, database_zone=db_zone,
                                         short_name=short_name, category=category)
        client.save()
        if client.pk:
            return redirect('home_dash')
        else:
            return redirect('add_device')


def search_clients(request):
    clients = models.ThinDevicesUnits.objects.all()
    clients_filter = ThinClientFilter(request.GET, queryset=clients)
    thins = clients_filter.qs
    context = {"clients": thins, "myfilter": clients_filter}
    return render(request, 'devices/search_clients.html', context=context)


def work_flow(request):
    return render(request, 'devices/work_flow.html')


def thin_uint(request, pk):
    thin = models.ThinDevicesUnits.objects.get(pk=pk)
    context = {"thin": thin}
    if request.method == 'POST':
        done = request.POST.get('devices_done')
        status = request.POST.get('status')
        thin.devices_done = done
        thin.status = status
        return redirect('search_clients')
    return render(request, 'devices/thin_clients.html', context=context)
