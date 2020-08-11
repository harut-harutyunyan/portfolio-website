# Generated by Django 3.1 on 2020-08-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200809_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=255)),
                ('image', models.ImageField(default='project_pics/default.jpg', upload_to='project_pics')),
                ('link_to_code', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('link_desc', models.CharField(blank=True, max_length=100)),
                ('skills', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
