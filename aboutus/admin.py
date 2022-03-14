from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from . import models
# Register your models here.
admin.site.register(models.AboutUs)
admin.site.register(models.LinkAcount)