# Generated by Django 2.2.4 on 2019-09-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_saledetail_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledetail',
            name='subtotal',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
