# Generated by Django 3.1 on 2020-09-20 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
    ]