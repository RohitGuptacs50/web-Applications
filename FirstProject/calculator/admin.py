from django.contrib import admin

# Register your models here.

from .models import Add


class CalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'n', 'm', 'res')

admin.site.register(Add, CalcAdmin)
