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
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


def home_dash(request):
    return render(request, 'devices/home-dash.html')


@login_required(login_url='login')
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


@login_required(login_url='login')
def search_clients(request):
    clients = models.ThinDevicesUnits.objects.all()
    clients_filter = ThinClientFilter(request.GET, queryset=clients)
    thins = clients_filter.qs
    context = {"clients": thins, "myfilter": clients_filter}
    return render(request, 'devices/search_clients.html', context=context)


def work_flow(request):
    return render(request, 'devices/work_flow.html')


@login_required(login_url='login')
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
        units = models.ThinDevicesUnits.objects.filter(status='مخزن')
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


@login_required(login_url='login')
def test(request):
    return render(request, 'devices/test.html')


def report(request):
    if request.method == "POST":
        status = request.POST.get('status')
        name = request.POST.get('name')
        template = get_template('uint_reports.html')
        units = models.ThinDevicesUnits.objects.filter(name__contains=name, status=status)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
            "devices": units,
            "topic": "تفاصيل العمل اليومى للوحدة  ",
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
    return render(request, 'devices/filterreport.html')


def delete_thin(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = models.ThinDevicesUnits.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def get_thin_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = models.ThinDevicesUnits.objects.filter(pk=id)
        qs_json = serializers.serialize('json', list(thin))
        return JsonResponse({"data": qs_json})


def update_thin(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        user = User.objects.get(pk=request.user.pk)
        name = request.POST.get('name')
        status = request.POST.get('status')
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = models.ThinDevicesUnits.objects.get(pk=update_id)
        thin.added_by = user
        thin.name = name
        thin.status = status
        thin.cdb = cdb
        thin.epg = epg
        thin.short_name = short_name
        thin.database_name = database_name
        thin.database_zone = database_zone
        thin.devices_done = devices_done
        thin.total_devices = total_devices
        thin.save()
        return JsonResponse({"data": 1})


def create_thin(request):
    if request.method == "POST" and request.is_ajax:
        user_obj = User.objects.get(pk=request.user.pk)
        name = request.POST.get('name')
        status = request.POST.get('status')
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = models.ThinDevicesUnits(added_by=user_obj, name=name, status=int(status), cdb=cdb, epg=epg,
                                       short_name=short_name,
                                       database_name=database_name
                                       , database_zone=database_zone, devices_done=devices_done,
                                       total_devices=total_devices)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def mainGrid(request):
    uts = models.ThinDevicesUnits.NAME_CHOICES
    model = models.ThinDevicesUnits.objects.all()
    clients_filter = ThinClientFilter(request.GET, queryset=model)
    thins = clients_filter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(thins, 8)
    try:
        thins = paginator.page(page)
    except PageNotAnInteger:
        thins = paginator.page(1)
    except EmptyPage:
        thins = paginator.page(paginator.num_pages)
    return render(request, 'devices/maingrid.html', context={"data": thins, 'units': uts})


def create_main(request):
    if request.method == "POST" and request.is_ajax:
        name = request.POST.get('name')
        build = request.POST.get('build')
        groupwork = request.POST.get('groupwork')
        twinte_five_percentgy = request.POST.get('twinte_five_percentgy')
        fifty_percentgy = request.POST.get('fifty_percentgy')
        catoperation = request.POST.get('catoperation')
        mangloc = request.POST.get('mangloc')
        center110 = request.POST.get('center110')
        center100 = request.POST.get('center100')
        seprated_thin = request.POST.get('seprated_thin')
        thin = models.ThinDevicesUnits(name=name, build=build, groupwork=groupwork,
                                       twinte_five_percentgy=twinte_five_percentgy, fifty_percentgy=fifty_percentgy,
                                       catoperation=catoperation
                                       , mangloc=mangloc, center110=center110,
                                       center100=center100, seprated_thin=seprated_thin)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def update_main(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        name = request.POST.get('name')
        build = request.POST.get('build')
        groupwork = request.POST.get('groupwork')
        twinte_five_percentgy = request.POST.get('twinte_five_percentgy')
        catoperation = request.POST.get('catoperation')
        mangloc = request.POST.get('mangloc')
        center110 = request.POST.get('center110')
        center100 = request.POST.get('center100')
        seprated_thin = request.POST.get('seprated_thin')
        thin = models.ThinDevicesUnits.objects.get(pk=update_id)
        thin.name = name
        thin.build = build
        thin.groupwork = groupwork
        thin.twinte_five_percentgy = twinte_five_percentgy
        thin.catoperation = catoperation
        thin.mangloc = mangloc
        thin.center110 = center110
        thin.center100 = center100
        thin.seprated_thin = seprated_thin
        thin.save()
        return JsonResponse({"data": 1})


def MainReport(request):
    if request.method == "POST":
        status = request.POST.get('status')
        name = request.POST.get('name')
        template = get_template('main_report.html')
        units = models.ThinDevicesUnits.objects.filter(name__contains=name, status=status)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
            "devices": units,
            "topic": "تفاصيل العمل اليومى للوحدة  ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('main_report.html', context)
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
    return render(request, 'devices/main_report_page.html')


@login_required(login_url='login')
def sara_grid(request):
    uts = models.ThinDevicesUnits.NAME_CHOICES
    qs = models.ThinDevicesUnits.objects.all()
    clients_filter = ThinClientFilter(request.GET, queryset=qs)
    thins = clients_filter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(thins, 8)
    try:
        thins = paginator.page(page)
    except PageNotAnInteger:
        thins = paginator.page(1)
    except EmptyPage:
        thins = paginator.page(paginator.num_pages)
    return render(request, 'devices/device.html', context={"data": thins, "units": uts})
