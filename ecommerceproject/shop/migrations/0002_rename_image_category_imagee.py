# Generated by Django 3.2.15 on 2022-10-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='imagee',
        ),
    ]
