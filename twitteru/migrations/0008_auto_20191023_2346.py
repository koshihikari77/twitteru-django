# Generated by Django 2.2.6 on 2019-10-23 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteru', '0007_auto_20191023_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='replayed_num',
            new_name='replied_num',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='replay_flag',
            new_name='reply_flag',
        ),
    ]
