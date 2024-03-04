from django.db import models
from customer.models import Customer

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10, verbose_name='placa', null=False)
    model = models.CharField(max_length=30, verbose_name='modelo', null=True)
    description = models.CharField(max_length=50, verbose_name='descricao', blank=True, null=True)
    customer_id = models.ForeignKey(Customer, related_name='vehicles', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.description
