# Generated by Django 3.1.1 on 2020-09-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoadmin',
            name='pincode',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]