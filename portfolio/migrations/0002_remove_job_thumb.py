# Generated by Django 3.1 on 2020-08-09 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='thumb',
        ),
    ]
