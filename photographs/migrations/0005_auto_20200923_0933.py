# Generated by Django 3.1.1 on 2020-09-23 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photographs', '0004_auto_20200921_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aerialphoto',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.RenameField(
            model_name='fineartphoto',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.RenameField(
            model_name='portraitphoto',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.RenameField(
            model_name='sportsphoto',
            old_name='id',
            new_name='painting_id',
        ),
    ]
