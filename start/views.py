# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from io import StringIO
from django.core.management import call_command
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import customer,statistics,distribution,owner,serial,payment,track
from .forms import login_form,owner_account_form,customer_account
import uuid

def index(request):
    return render(request,'start/index.html',{})

def customers(request):
    if request.method == 'POST':
        token = int(request.POST.get('token'))
        customer_object = get_object_or_404(customer, token=token)
        statistics_object = get_object_or_404(statistics, customer=customer_object)
        distribution_object = distribution.objects.filter(customer=customer_object)
        context = {'customer_object': customer_object, 'statistics': statistics_object,
                   'distribution': distribution_object}
        return render(request, 'start/record_customer.html', context)
    all_customer = customer.objects.all()
    context = {'all_customer' : all_customer}
    return render(request,'start/customer.html',context)

def customer_by_token(request,token):
    token = int(token)
    customer_object = get_object_or_404(customer, token=token)
    statistics_object = get_object_or_404(statistics, customer=customer_object)
    distribution_object = distribution.objects.filter(customer=customer_object)
    context = {'customer_object': customer_object , 'statistics' : statistics_object ,
               'distribution' : distribution_object}
    return render(request, 'start/record_customer.html', context)

def owner_login(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            return redirect('/owner')
    except:
        if request.method == 'POST':
            form = login_form(request.POST)
            if form.is_valid():
                username = owner_object.username
                password = owner_object.password
                form_username = form.cleaned_data['username']
                form_password = form.cleaned_data['password']
                if username == form_username and password == form_password:
                    owner_object.session_key = uuid.uuid1().hex
                    owner_object.save()
                    request.session[owner_object.session_key] = True
                    return redirect('/owner')
                else:
                    return HttpResponse("Access Denied")
        else:
            form = login_form()
            context = {'form': form}
            return render(request, 'start/login.html', context)


def owner_page(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            return render(request , 'start/owner.html' , {})
    except:
        return HttpResponse("Session Logout")

def logout(request):
    owner_object = owner.objects.get()
    owner_object.session_key = ""
    owner_object.save()
    request.session.flush()
    return redirect('/owner/login')

def owner_account(request):
    owner_object = owner.objects.get()
    if request.method == 'POST':
        post_form = owner_account_form(request.POST)
        if post_form.is_valid():
            owner_object.name = post_form.cleaned_data['name']
            owner_object.address = post_form.cleaned_data['address']
            owner_object.contact1 = post_form.cleaned_data['contact1']
            owner_object.contact2 = post_form.cleaned_data['contact2']
            owner_object.L = post_form.cleaned_data['L']
            owner_object.M = post_form.cleaned_data['M']
            owner_object.H = post_form.cleaned_data['H']
            owner_object.username = post_form.cleaned_data['username']
            owner_object.password = post_form.cleaned_data['password']
            owner_object.save()
    try:
        if request.session[owner_object.session_key] == True:
            form = owner_account_form(initial={'name': owner_object.name,
                                               'address': owner_object.address,
                                               'contact1': owner_object.contact1,
                                               'contact2': owner_object.contact2,
                                               'L': owner_object.L,
                                               'M': owner_object.M,
                                               'H': owner_object.H,
                                               'username': owner_object.username,
                                               'password': owner_object.password})
            context = {'form': form}
            return render(request, 'start/owner_account.html', context)
    except:
        return HttpResponse("Session Logout")

def customer_add(request):
    owner_object = owner.objects.get()
    if request.method == 'POST':
        form = customer_account(request.POST)
        if form.is_valid():
            customer_object = customer()
            customer_object.name = form.cleaned_data['name']
            customer_object.address = form.cleaned_data['address']
            customer_object.contact1 = form.cleaned_data['contact1']
            customer_object.contact2 = form.cleaned_data['contact2']
            customer_object.save()
    try:
        if request.session[owner_object.session_key] == True:
            form = customer_account()
            context = {'form' : form}
            return render(request , 'start/customer_add.html' , context)
    except:
        return HttpResponse("Session Logout")

def display_all_serials(request):
    serial_object = serial.objects.order_by('serial')
    s = ""
    for x in serial_object:
        s=s+str(x.serial)+" "
    return HttpResponse(s)

def distribute(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            if request.method == 'POST':
                token = int(request.POST.get('token'))
                customer_object = get_object_or_404(customer, token=token)
                statistics_object = get_object_or_404(statistics, customer=customer_object)
                distribution_object = distribution.objects.filter(customer=customer_object)
                context = {'customer_object': customer_object, 'statistics': statistics_object,
                   'distribution': distribution_object , 'owner_object' : owner_object}
                return render(request, 'start/distribute.html', context)
            all_customer = customer.objects.all()
            context = {'all_customer' : all_customer}
            return render(request,'start/distribute_customer.html',context)
    except:
        return HttpResponse("Session Logout")

def distribute_by_token(request,token):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
           token = int(token)
           customer_object = get_object_or_404(customer, token=token)
           statistics_object = get_object_or_404(statistics, customer=customer_object)
           distribution_object = distribution.objects.filter(customer=customer_object)
           context = {'customer_object': customer_object , 'statistics' : statistics_object ,
               'distribution' : distribution_object , 'owner_object' : owner_object}
           return render(request, 'start/distribute.html', context)
    except:
        return HttpResponse("Session Logout")

def distribute_save(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
           if request.method == "POST":
              token = int(request.POST.get("token"))
              amount = float(request.POST.get("amount"))
              money = float(request.POST.get("money"))
              customer_object = get_object_or_404(customer,token=token)
              track_object = get_object_or_404(track,customer=customer_object)
              track_object.bool = True
              track_object.save()
              object = distribution(amount=amount,money=money,customer=customer_object)
              object.save()
              serial_object = get_object_or_404(serial,customer=customer_object)
              new_serial = serial_object.serial+1
              loop_object = serial.objects.all()
              first = 0
              second = 0
              inc = 1
              for x in loop_object:
                 if inc == 1:
                    first = x.serial
                 second = x.serial
                 inc+=1
              if new_serial > second:
                 new_serial = first
              serial_object3 = get_object_or_404(serial,serial=new_serial)
              new_token = serial_object3.customer.token
              str_token = str(new_token)
              redirect_str = "/distribute/"+str_token
              return redirect(redirect_str)
    except:
        return HttpResponse("Session Logout")

def payment_save(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
           if request.method == "POST":
              token = int(request.POST.get("token"))
              money = float(request.POST.get("money"))
              customer_object = get_object_or_404(customer,token=token)
              object = payment(money=money,customer=customer_object)
              object.save()
              str_token = str(token)
              redirect_str = "/distribute/"+str_token
              return redirect(redirect_str)
    except:
        return HttpResponse("Session Logout")

def update(request):
    owner_object = owner.objects.get()
    try:
        if request.method == 'POST':
            token = request.POST['token']
            redirect_str = '/update/'+str(token)
            return redirect(redirect_str)
        if request.session[owner_object.session_key] == True:
            all_customer = customer.objects.all()
            context = {'all_customer': all_customer}
            return render(request, 'start/update_customer.html', context)
    except:
        return HttpResponse("Session Logout")
def update_by_token(request,token):
    owner_object = owner.objects.get()
    if request.method == 'POST':
        form = customer_account(request.POST)
        if (form.is_valid()):
            customer_object = get_object_or_404(customer,token=token)
            customer_object.name = form.cleaned_data['name']
            customer_object.address = form.cleaned_data['address']
            customer_object.contact1 = form.cleaned_data['contact1']
            customer_object.contact2 = form.cleaned_data['contact2']
            customer_object.save(update_fields=['name','address','contact1','contact2'])
            redirect_str = '/update/'+str(token)
            return redirect(redirect_str)
    try:
        if request.session[owner_object.session_key] == True:
            customer_object = get_object_or_404(customer,token=token)
            form = customer_account(initial={'name': customer_object.name,
                                               'address': customer_object.address,
                                               'contact1': customer_object.contact1,
                                               'contact2': customer_object.contact2,
                                               })
            context = {'form' : form}
            return render(request , 'start/update.html' , context)

    except:
        return HttpResponse("Session Logout")

def track_state(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            return render(request , 'start/track_choose.html' , {})
    except:
        return HttpResponse("Session Logout")

def start_track(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            customer_objects = customer.objects.all()
            for x in customer_objects:
                track_object = track(customer=x)
                track_object.save()
        return redirect('')
    except:
        return HttpResponse("Session Logout")

def end_track(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            ob = track()
            track.delete_everything(ob)
            return redirect('')
    except:
        return HttpResponse("Session Logout")

def track_place(request):
    owner_object = owner.objects.get()
    try:
        if request.session[owner_object.session_key] == True:
            serial_object = serial.objects.all()
            l = []
            for x in serial_object:
                object = get_object_or_404(track , customer = x.customer)
                l.append(object)
            context = {'track_objects' : l}
            return render(request , 'start/track.html' , context)
    except:
        return HttpResponse("Session Logout")