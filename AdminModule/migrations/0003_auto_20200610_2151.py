# Generated by Django 3.0.6 on 2020-06-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminModule', '0002_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='Users',
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]
