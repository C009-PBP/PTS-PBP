# Generated by Django 4.1 on 2022-10-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi_calculator', '0002_alter_bmi_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmi',
            name='jenis_kelamin',
        ),
        migrations.AddField(
            model_name='bmi',
            name='bmi_result',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bmi',
            name='deskripsi_hasil',
            field=models.TextField(default='Belum diketahui'),
        ),
        migrations.AddField(
            model_name='bmi',
            name='keterangan_tambahan',
            field=models.TextField(default='Perhitungan BMI ini ditujukan untuk orang dewasa berusia lebih dari 19 tahun. Karena faktor pertumbuhan yang terus menerus terjadi secara cepat, perhitungan BMI bagi orang berusia di bawah 19 tahun akan berdasar pada relativitas hasil BMI terhadap populasi dengan umur yang sama.'),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='berat',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='date_created',
            field=models.DateField(default=1),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='tinggi',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='umur',
            field=models.BigIntegerField(default=1),
        ),
    ]
