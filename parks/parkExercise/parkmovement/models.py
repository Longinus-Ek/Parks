from django.db import models

class DateTimeEntry(models.Model):
    entry_date = models.DateTimeField(verbose_name='dataIn', null=False)

class DateTimeExit(models.Model):
    exit_date = models.DateTimeField(verbose_name='dataFn', null=False)

class Parkmovement(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.ForeignKey(DateTimeEntry, on_delete=models.CASCADE, related_name='parkmovement_entry')
    exit_date = models.ForeignKey(DateTimeExit, on_delete=models.CASCADE, related_name='parkmovement_exit')
    vehicle_id = models.IntegerField(verbose_name='veiculoID', null=False)
    value = models.FloatField(verbose_name='valor', null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.vehicle_id
