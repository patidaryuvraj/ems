# Generated by Django 4.1.4 on 2023-05-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employee_age_alter_employee_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(),
        ),
    ]