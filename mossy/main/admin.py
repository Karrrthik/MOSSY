from django.contrib import admin
from .models import Files

class Adminmain(admin.ModelAdmin):
    list_display = ('file', 'filename')

# Register your models here.
admin.site.register(Files, Adminmain)