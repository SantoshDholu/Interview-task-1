# Generated by Django 3.1.5 on 2021-03-22 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_feedback_feedback_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback_1',
            field=models.TextField(default=datetime.time),
            preserve_default=False,
        ),
    ]
