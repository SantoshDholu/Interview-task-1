# Generated by Django 3.1.5 on 2021-03-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210322_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback1',
            new_name='feedback',
        ),
    ]