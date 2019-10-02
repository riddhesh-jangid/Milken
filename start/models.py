# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.shortcuts import render,get_object_or_404,redirect

class owner(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField()
    L = models.IntegerField()
    M = models.IntegerField()
    H = models.IntegerField()
    pin = models.IntegerField(default=0000)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    session_key = models.CharField(max_length=50,default="",null=True,blank=True)


class customer(models.Model):
    token = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=100)
    selection = models.CharField(max_length=1,default='M')
    def __str__(self):
        return str(self.token)

class serial(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    serial = models.IntegerField(unique=True,default=-1)

class distribution(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    money = models.FloatField()
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)

class payment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    money = models.FloatField()
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)

class statistics(models.Model):
    remaining = models.FloatField(default=0.0)
    last_payment = models.FloatField(default=0.0)
    last_payment_date = models.DateTimeField(blank=True,null=True)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)

class track(models.Model):
    bool = models.BooleanField(default=False)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)

    def delete_everything(self):
        track.objects.all().delete()

@receiver(post_save,sender = customer)
def recieve_customer_signal(sender,instance,**Kwarge):
    bool = False
    customer_object = get_object_or_404(customer,token=instance.token)
    print (customer_object.token)
    try:
        statistics_object = get_object_or_404(statistics,customer=customer_object)
    except:
        bool = True

    if bool:
        create_statistics = statistics(customer=instance)
        create_statistics.save()
        create_serial = serial(customer=instance)
        objects_serial = serial.objects.order_by('serial')
        count = 1
        for object in objects_serial:
            if object.serial == count:
                pass
            else:
                create_serial.serial = count
                break
            count += 1
        if create_serial.serial == -1 and count == 1:
            create_serial.serial = 1
        if create_serial.serial == -1 and count > 1:
            create_serial.serial = count
        create_serial.save()

@receiver(post_save,sender = distribution)
def receive_distribution_signal(sender,instance,**Kwarge):
    object_statistics = statistics.objects.get(customer=instance.customer)
    object_statistics.remaining = object_statistics.remaining + instance.money
    object_statistics.save()

@receiver(post_save,sender = payment)
def receive_payment_signal(sender,instance,**Kwarge):
    object_payment = statistics.objects.get(customer=instance.customer)
    object_payment.remaining = object_payment.remaining - instance.money
    object_payment.last_payment = instance.money
    object_payment.last_payment_date = instance.date
    object_payment.save()
