# Generated by Django 4.1.4 on 2023-05-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
