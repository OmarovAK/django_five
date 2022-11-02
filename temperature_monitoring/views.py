from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serialisers import SensorSerial, SensorSerialAdd, MonitorSerialAdd


@api_view(['GET'])
def monitor_view(request):
    sensor = Sensor.objects.all()
    data = SensorSerial(sensor, many=True)

    return Response(data.data)


@api_view(['GET', 'PATCH'])
def monitor_view_one(request, pk):
    if request.method == "GET":
        sensor = Sensor.objects.get(id=pk)
        data = SensorSerial(sensor, many=False)
        return Response(data.data)
    if request.method == "PATCH":
        sensor = Sensor.objects.get(id=pk)
        print(sensor)
        serial = SensorSerialAdd(data=request.data, instance=sensor)
        serial.is_valid()
        serial.save()
        return Response({"post": serial.data})


class AddMonitor(APIView):
    def post(self, request):
        serializer = SensorSerialAdd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, *args, **kwargs):
        id_ = kwargs.get('pk', None)
        instance = Sensor.objects.get(pk=id_)
        serial = SensorSerialAdd(data=request.data, instance=instance)
        serial.is_valid()
        serial.save()
        return Response(status=200)


class AddTemps(APIView):
    def post(self, request):
        serialiser = MonitorSerialAdd(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(status=201)
        else:
            return Response(status=400)
