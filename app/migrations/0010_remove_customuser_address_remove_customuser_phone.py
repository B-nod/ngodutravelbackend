# Generated by Django 5.1.2 on 2024-10-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
