# Generated by Django 4.0.4 on 2022-05-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_img8'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default-pic.png', null=True, upload_to='profile_pics'),
        ),
    ]
