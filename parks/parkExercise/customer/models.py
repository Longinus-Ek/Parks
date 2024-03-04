from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='nome', null=False)
    card_id = models.CharField(max_length=10, verbose_name='cardID', null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
