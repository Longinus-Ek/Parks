# Generated by Django 5.0.2 on 2024-03-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('card_id', models.CharField(max_length=10, null=True, verbose_name='cardID')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
