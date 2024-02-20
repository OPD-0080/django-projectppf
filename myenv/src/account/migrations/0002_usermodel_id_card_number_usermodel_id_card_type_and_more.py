# Generated by Django 5.0.2 on 2024-02-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='ID_card_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='ID_card_type',
            field=models.CharField(blank=True, choices=[('National ID', 'National ID'), ('Voters ID', 'Voters ID'), ('Passport ID', 'Passport ID')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='ID_photo_back',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='ID_photo_front',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='department',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='otp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='photo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='userID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]