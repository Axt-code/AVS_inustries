# Generated by Django 3.1.5 on 2021-04-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210409_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_spec1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec4',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec5',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec6',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec7',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_spec8',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
    ]
