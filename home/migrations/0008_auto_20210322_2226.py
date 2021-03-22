# Generated by Django 3.1.5 on 2021-03-22 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_1',
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback',
            field=models.Field(default=datetime.time),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='contactus',
            table='contact',
        ),
    ]
