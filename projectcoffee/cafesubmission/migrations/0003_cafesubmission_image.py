# Generated by Django 4.1.7 on 2023-03-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafesubmission', '0002_remove_cafesubmission_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafesubmission',
            name='image',
            field=models.ImageField(default='coffee_shop_images/default.jpg', upload_to='coffee_shop_images'),
        ),
    ]
