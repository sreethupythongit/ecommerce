# Generated by Django 3.2.15 on 2022-10-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_image_category_imagee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='imagee',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
    ]
