# Generated by Django 4.2.1 on 2023-06-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_friends_user_friends_count_friendshiprequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_count',
            field=models.IntegerField(default=0),
        ),
    ]
