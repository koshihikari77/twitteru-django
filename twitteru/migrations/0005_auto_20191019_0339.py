# Generated by Django 2.2.6 on 2019-10-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteru', '0004_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='media'),
        ),
    ]