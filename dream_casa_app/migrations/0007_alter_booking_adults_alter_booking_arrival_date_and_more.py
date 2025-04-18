# Generated by Django 5.0.7 on 2024-11-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_casa_app', '0006_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
