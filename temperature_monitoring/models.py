from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    def __str__(self):
        print(type(self.title))
        return str(self.title)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Monitoring(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='monitoring')
    temperature = models.IntegerField(verbose_name='Температура')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        name = f'{self.id_sensor}'
        return name

    class Meta:
        verbose_name = 'измерение температуры'
        verbose_name_plural = 'измерения температуры'
