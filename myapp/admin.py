from django.contrib import admin
from .models import imagemodel
# Register your models here.
@admin.register(imagemodel)
class adminform(admin.ModelAdmin):
    list_display = ['id','photo','date']
