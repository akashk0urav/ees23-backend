# Generated by Django 3.2.7 on 2022-12-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracount',
            name='year',
            field=models.CharField(choices=[('FIRST', '1st year'), ('SECOND', '2nd year'), ('THIRD', '3rd year'), ('FORTH', '4th year'), ('FIFTH', '5th year')], max_length=20),
        ),
    ]