# Generated by Django 4.1.7 on 2023-03-07 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafesubmission', '0005_delete_rating_cafesubmission_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafesubmission',
            name='approved',
        ),
    ]
