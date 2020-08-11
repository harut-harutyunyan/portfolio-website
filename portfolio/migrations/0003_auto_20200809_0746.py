# Generated by Django 3.1 on 2020-08-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_job_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='details',
            new_name='thumb',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=25),
            preserve_default=False,
        ),
    ]
