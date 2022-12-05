# Generated by Django 4.1.3 on 2022-11-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
                ('details', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100)),
            ],
        ),
    ]