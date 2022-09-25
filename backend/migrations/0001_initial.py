# Generated by Django 4.1.1 on 2022-09-25 18:55

import backend.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='MediaSurf/media/categorydata')),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('videos', models.IntegerField(blank=True, default=0, null=True)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('recommended_videos', models.CharField(blank=True, max_length=1024, null=True)),
                ('new_videos', models.CharField(blank=True, max_length=1024, null=True)),
                ('favorite_videos', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64, unique=True)),
                ('url', models.URLField(max_length=300)),
                ('open_tab', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('is_favourite', models.BooleanField(blank=True, default=False, null=True)),
                ('bio', models.CharField(blank=True, max_length=1024, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('videos', models.IntegerField(blank=True, default=0, null=True)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('poster', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_poster)),
                ('banner', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_banner)),
                ('tags', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=512, unique=True)),
                ('title', models.CharField(max_length=1024)),
                ('categories', models.CharField(blank=True, max_length=512, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('cast', models.CharField(blank=True, max_length=512, null=True)),
                ('favourite', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('poster', models.FileField(blank=True, null=True, upload_to='')),
                ('subtitle', models.FileField(blank=True, null=True, upload_to='')),
                ('preview', models.FileField(blank=True, null=True, upload_to='')),
                ('scrubber', models.FileField(blank=True, null=True, upload_to='')),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('resolution', models.CharField(blank=True, max_length=30, null=True)),
                ('search_text', models.CharField(blank=True, max_length=1024, null=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('tags', models.CharField(blank=True, max_length=512, null=True)),
                ('series', models.CharField(blank=True, max_length=512, null=True)),
                ('episode', models.IntegerField(blank=True, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('last_viewed', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
