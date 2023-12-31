# Generated by Django 4.1.4 on 2023-05-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employees_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default='1')),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=55, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
