# Generated by Django 4.1.3 on 2022-11-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=150), max_length=150),
        ),
    ]
