from rest_framework import serializers
from .models import Sensor, Monitoring


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = [
            'temperature', 'date'
        ]


class SensorSerial(serializers.ModelSerializer):
    monitoring = MonitorSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = [
            'title', 'description', 'monitoring', 'id'
        ]


class SensorSerialAdd(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            'title', 'description'
        ]

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get("description")
        instance.save()
        return instance


class MonitorSerialAdd(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = [
            'id_sensor', 'temperature', 'date'
        ]

        def create(self, validated_data):
            return Monitoring.objects.create(**validated_data)
