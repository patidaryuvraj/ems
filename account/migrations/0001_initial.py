# Generated by Django 4.1.4 on 2023-05-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=55)),
                ('lname', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=55)),
                ('mobile', models.CharField(max_length=15)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
