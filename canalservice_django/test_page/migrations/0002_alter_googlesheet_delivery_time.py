# Generated by Django 4.0.4 on 2022-05-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlesheet',
            name='delivery_time',
            field=models.DateTimeField(),
        ),
    ]
