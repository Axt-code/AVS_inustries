# Generated by Django 3.1.5 on 2021-03-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210316_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='machines',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]