# Generated by Django 3.0.3 on 2020-09-14 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
