# Generated by Django 4.1 on 2022-10-30 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_rename_description_review_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.TextField(default=''),
        ),
    ]