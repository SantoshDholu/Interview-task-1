# Generated by Django 3.1.5 on 2021-03-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('pass1', models.CharField(max_length=30)),
                ('pass2', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]
