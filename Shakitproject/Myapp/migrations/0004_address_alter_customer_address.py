# Generated by Django 5.1.3 on 2024-12-02 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_alter_customer_customer_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('subdistrict', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100)),
                ('district', models.CharField(choices=[('1', 'District 1'), ('2', 'District 2'), ('3', 'District 3')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.address'),
        ),
    ]
