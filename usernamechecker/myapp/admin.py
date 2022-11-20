from django.contrib import admin
from .models import Userdata
# Register your models here.
@admin.register(Userdata)
class Useradmin(admin.ModelAdmin):
    list_display= ('id','username')