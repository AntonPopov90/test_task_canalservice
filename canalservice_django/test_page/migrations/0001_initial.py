# Generated by Django 4.0.4 on 2022-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('order_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('delivery_time', models.DateField()),
                ('price_in_rub', models.TextField()),
            ],
        ),
    ]
