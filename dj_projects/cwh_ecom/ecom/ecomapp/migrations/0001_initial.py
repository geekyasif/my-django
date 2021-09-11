# Generated by Django 3.2 on 2021-04-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_detail', models.TextField(blank=True)),
                ('created', models.DateField()),
            ],
        ),
    ]
