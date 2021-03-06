# Generated by Django 2.2.6 on 2019-11-02 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitteru', '0010_auto_20191029_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='followed_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_user_relation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_user_relation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post_relation', to='twitteru.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liking_user_relation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='replied_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied_post_relation', to='twitteru.Post'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='replying_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replying_post_relation', to='twitteru.Post'),
        ),
    ]
