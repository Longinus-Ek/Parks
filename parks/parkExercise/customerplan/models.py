from django.db import models
from customer.models import Customer
from plan.models import Plan

class Customer_plan(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, related_name='customer_plans', on_delete=models.CASCADE, null=True)
    plan_id = models.ForeignKey(Plan, related_name='customer_plans', on_delete=models.CASCADE, null=True)
    due_date = models.DateTimeField(verbose_name='dataMn', null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.customer_id} - {self.plan_id}"
