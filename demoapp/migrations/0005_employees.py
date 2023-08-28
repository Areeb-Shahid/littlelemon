# Generated by Django 4.2.4 on 2023-08-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('shift', models.IntegerField()),
            ],
        ),
    ]
