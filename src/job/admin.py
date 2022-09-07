from unicodedata import category
from django.contrib import admin
# Django model field : html widget, validation, db size
# Register your models here.
from .models import job,category,apply
admin.site.register(job)
admin.site.register(category)
admin.site.register(apply)

