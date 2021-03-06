# Generated by Django 4.0.5 on 2022-06-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('identity', models.CharField(max_length=15)),
                ('datebirth', models.DateField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='People_phones',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_people', models.IntegerField()),
                ('phonenumber', models.CharField(max_length=15)),
            ],
        ),
    ]
