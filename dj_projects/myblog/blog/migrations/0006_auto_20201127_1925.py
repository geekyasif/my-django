# Generated by Django 3.1.3 on 2020-11-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='sno',
            new_name='commentid',
        ),
    ]