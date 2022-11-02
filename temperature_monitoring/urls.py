from django.urls import path

from temperature_monitoring.views import monitor_view, monitor_view_one, AddMonitor, AddTemps

app_name = 'temp'
urlpatterns = [
    path('all/', monitor_view),
    path('<int:pk>/', monitor_view_one),
    path('add/', AddMonitor.as_view()),
    path('edit/<int:pk>/', AddMonitor.as_view()),
    path('add_temp/', AddTemps.as_view()),

]
