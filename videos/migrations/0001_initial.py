# Generated by Django 3.1 on 2020-09-20 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('course_name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('session', models.IntegerField()),
                ('link', models.URLField(max_length=500)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.professor')),
            ],
        ),
    ]