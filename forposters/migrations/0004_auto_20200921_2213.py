# Generated by Django 3.1.1 on 2020-09-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forposters', '0003_auto_20200921_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignposters',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignposters',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaignposters',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignposters',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaignposters',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corporateposters',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='corporateposters',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corporateposters',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='corporateposters',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corporateposters',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalposters',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='politicalposters',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalposters',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='politicalposters',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalposters',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showposters',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showposters',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showposters',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showposters',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showposters',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]
