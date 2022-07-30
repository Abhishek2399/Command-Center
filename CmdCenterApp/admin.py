from django.contrib import admin
from .models import *


# admin site display and search settings

class DataCenter_Setting(admin.ModelAdmin):
    search_fields = ['datacenter_name']
    list_display = ['datacenter_name']

class Server_Setting(admin.ModelAdmin):
    search_fields = ['server_name', 'datacenter__datacenter_name']
    list_display = ['server_name', 'datacenter']

class Application_Setting(admin.ModelAdmin):
    search_fields = ['app_name', 'server__server_name', 'server__datacenter__datacenter_name']
    list_display = ['app_name', 'server']

class Action_Setting(admin.ModelAdmin):
    search_fields = ['action_name', 'application__app_name', 'application__server__server_name', 'application__server__datacenter__datacenter_name']
    list_display = ['action_name', 'application']



# Register your models here.
admin.site.register(DataCenter, DataCenter_Setting)
admin.site.register(Server, Server_Setting)
admin.site.register(Application, Application_Setting)
admin.site.register(Action, Action_Setting)