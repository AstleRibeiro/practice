# Generated by Django 3.1 on 2020-09-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicnav', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acrylicpainting',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.RenameField(
            model_name='inkpainting',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.RenameField(
            model_name='pastelpainting',
            old_name='id',
            new_name='painting_id',
        ),
        migrations.AlterField(
            model_name='abstractpainting',
            name='painting_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]