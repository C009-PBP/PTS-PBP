# Generated by Django 4.1 on 2022-10-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi_calculator', '0003_remove_bmi_jenis_kelamin_bmi_bmi_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='berat',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='bmi_result',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='date_created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='tinggi',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='umur',
            field=models.BigIntegerField(),
        ),
    ]