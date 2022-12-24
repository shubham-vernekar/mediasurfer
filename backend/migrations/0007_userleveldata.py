# Generated by Django 4.1.1 on 2022-12-24 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_series_cast_series_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_videos', models.IntegerField(blank=True, default=0, null=True)),
                ('unsupported_videos', models.IntegerField(blank=True, default=0, null=True)),
                ('update_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('scan_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('volume_level', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
