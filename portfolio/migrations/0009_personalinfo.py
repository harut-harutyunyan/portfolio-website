# Generated by Django 3.1 on 2020-08-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20200811_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='har8unyan@gmail.com', max_length=254)),
                ('avatar', models.ImageField(default='personal/default.jpg', upload_to='personal')),
                ('photo', models.ImageField(upload_to='personal')),
                ('signature', models.CharField(max_length=255)),
                ('home_message', models.TextField()),
                ('about_text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
