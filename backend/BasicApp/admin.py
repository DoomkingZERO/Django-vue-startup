from django.contrib import admin

from .models import PageVisit, SimplePageVisit

admin.site.register(PageVisit)
admin.site.register(SimplePageVisit)
