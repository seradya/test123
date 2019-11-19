from django.contrib import admin
from .models import Client, Service


class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]

    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]

    class Meta:
        model = Service

admin.site.register(Service, ServiceAdmin)