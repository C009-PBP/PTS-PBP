# Generated by Django 4.1 on 2022-10-29 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='description',
        ),
    ]