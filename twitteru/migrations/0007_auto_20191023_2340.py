# Generated by Django 2.2.6 on 2019-10-23 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteru', '0006_auto_20191020_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='replayed_post',
            new_name='replied_post',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='replaying_post',
            new_name='replying_post',
        ),
    ]
