from django.contrib import admin
from .models import Sensor, Monitoring


@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['description']


@admin.register(Monitoring)
class AdminMonitoring(admin.ModelAdmin):
    list_display = ['id', 'id_sensor', 'temperature', 'date']
    list_filter = ['date', 'id_sensor', ]
