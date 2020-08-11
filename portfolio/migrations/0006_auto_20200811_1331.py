# Generated by Django 3.1 on 2020-08-11 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='dates',
        ),
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
