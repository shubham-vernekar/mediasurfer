# Generated by Django 4.1.1 on 2023-01-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_create_trigger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
