# Generated by Django 4.1.4 on 2023-05-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=25, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
    ]