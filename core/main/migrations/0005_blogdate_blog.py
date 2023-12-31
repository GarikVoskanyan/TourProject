# Generated by Django 4.2.3 on 2023-09-18 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Blog Date')),
            ],
            options={
                'verbose_name': 'Blog Date',
                'verbose_name_plural': 'Blog Date',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_date', to='main.blogdate')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
