# Generated by Django 4.0.5 on 2022-06-07 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
