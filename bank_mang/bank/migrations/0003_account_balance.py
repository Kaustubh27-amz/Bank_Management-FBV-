# Generated by Django 3.0.3 on 2020-09-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_remove_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
