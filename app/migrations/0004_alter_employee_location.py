# Generated by Django 4.2 on 2023-04-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_employee_join_date_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(default='Unknow', max_length=50),
        ),
    ]
