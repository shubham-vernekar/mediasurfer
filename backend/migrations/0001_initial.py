# Generated by Django 4.1.1 on 2022-10-21 15:45

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
                ('poster', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_category_poster)),
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
            name='Series',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('videos', models.IntegerField(blank=True, default=0, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
