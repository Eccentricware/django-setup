# Generated by Django 3.2.7 on 2021-10-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0002_alter_userdetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='show_age',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='show_weight',
            field=models.BooleanField(default=False),
        ),
    ]