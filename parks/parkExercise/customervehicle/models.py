from django.db import models
from vehicle.models import Vehicle
from customer.models import Customer

class CustomerVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, related_name='customer_vehicles', on_delete=models.CASCADE, null=True)
    customer_id = models.ForeignKey(Customer, related_name='customer_vehicles', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.customer_id.name} - {self.vehicle_id.plate}"
