# Generated by Django 4.1.7 on 2023-03-07 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafesubmission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafesubmission',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cafesubmission',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cafesubmission',
            name='phone',
        ),
        migrations.AddField(
            model_name='cafesubmission',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cafesubmission',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafesubmission',
            name='submitted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cafesubmission',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cafesubmission',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cafesubmission',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]