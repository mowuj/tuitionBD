# Generated by Django 4.1.3 on 2022-11-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0010_class_in_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='class_in',
            field=models.ManyToManyField(related_name='class_set', to='tuition.class_in'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ManyToManyField(related_name='subject_set', to='tuition.subject'),
        ),
    ]