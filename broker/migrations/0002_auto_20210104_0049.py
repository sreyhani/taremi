# Generated by Django 2.2.7 on 2021-01-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='deadline',
            field=models.DateField(verbose_name='deadline'),
        ),
    ]
