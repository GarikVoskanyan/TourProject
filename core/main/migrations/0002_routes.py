# Generated by Django 4.2.3 on 2023-09-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
                ('title1', models.CharField(max_length=255, verbose_name='Slide Title')),
                ('title2', models.CharField(max_length=255, verbose_name='Slide Title')),
                ('text', models.TextField(verbose_name='Slide Text')),
            ],
            options={
                'verbose_name': 'Routes',
                'verbose_name_plural': 'Routes',
            },
        ),
    ]
