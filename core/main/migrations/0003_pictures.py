# Generated by Django 4.2.3 on 2023-09-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_routes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Pictures',
                'verbose_name_plural': 'Pictures',
            },
        ),
    ]
