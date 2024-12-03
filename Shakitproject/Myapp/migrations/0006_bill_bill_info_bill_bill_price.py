# Generated by Django 5.1.3 on 2024-12-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0005_alter_address_district_alter_address_subdistrict_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_info',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]