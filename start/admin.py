# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import owner,customer,distribution,payment,statistics,serial,track

admin.site.register(owner)
admin.site.register(customer)
admin.site.register(distribution)
admin.site.register(payment)
admin.site.register(statistics)
admin.site.register(serial)
admin.site.register(track)