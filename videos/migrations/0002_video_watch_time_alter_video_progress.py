# Generated by Django 4.1.1 on 2022-12-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='watch_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='progress',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
