# Generated by Django 4.0.5 on 2022-06-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_soldproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldproduct',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
