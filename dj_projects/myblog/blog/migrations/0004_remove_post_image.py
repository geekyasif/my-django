# Generated by Django 3.1.3 on 2020-11-25 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
