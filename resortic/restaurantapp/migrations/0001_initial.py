# Generated by Django 4.2.4 on 2023-09-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restb',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('ctime', models.CharField(max_length=30)),
                ('non', models.CharField(max_length=30)),
                ('veg', models.CharField(max_length=30)),
                ('re_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
