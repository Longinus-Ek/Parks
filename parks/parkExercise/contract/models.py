from django.db import models

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, verbose_name='descricao', null=False)
    max_value = models.FloatField(verbose_name='valorMax', null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.description
    
class Contract_rule(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, related_name='contract_rules', on_delete=models.CASCADE, null=True)
    until = models.IntegerField(verbose_name='until', null=False)
    value = models.FloatField(verbose_name='valor', null=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.contract_id} - {self.until}"
