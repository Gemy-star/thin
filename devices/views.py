from django.shortcuts import render, redirect
from thinclients.utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from users.models import User
from . import models
from .filters import ThinClientFilter
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers


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


class ClientsAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('allclients_reports.html')
        units = models.ThinDevicesUnits.objects.filter(status=1)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
            "devices": units,
            "topic": "تقرير جرد المستودع  ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('allclients_reports.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class ClientsTodayReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('thinclients_reports.html')
        units = models.ThinDevicesUnits.objects.filter(status=2)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
            "devices": units,
            "topic": "تفاصيل العمل اليومى  ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('thinclients_reports.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def report(request):
    if request.method == "POST":
        status = request.POST.get('status')
        name = request.POST.get('name')
        template = get_template('uint_reports.html')
        units = models.ThinDevicesUnits.objects.filter(name__contains=name, status=int(status))
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
            "devices": units,
            "topic": "تفاصيل العمل اليومى  ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('uint_reports.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    return render(request, 'devices/thinclients.html')
