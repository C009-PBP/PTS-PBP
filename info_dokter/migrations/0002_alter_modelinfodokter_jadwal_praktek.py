# Generated by Django 4.1 on 2022-10-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_dokter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelinfodokter',
            name='jadwal_praktek',
            field=models.TextField(),
        ),
    ]