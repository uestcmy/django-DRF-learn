# Generated by Django 3.0.3 on 2020-02-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=128, verbose_name='IP')),
                ('dev_name', models.CharField(max_length=128, verbose_name='Device_name')),
                ('vendor', models.CharField(max_length=128, verbose_name='Vendor')),
                ('model', models.CharField(max_length=128, verbose_name='Model')),
                ('series', models.CharField(max_length=128, verbose_name='Series')),
            ],
        ),
    ]