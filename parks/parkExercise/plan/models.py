from django.db import models

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, verbose_name='descricao', null=False)
    value = models.FloatField(verbose_name='valor', null=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.description
