# Generated by Django 3.2.6 on 2021-08-19 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('name',)},
        ),
    ]
