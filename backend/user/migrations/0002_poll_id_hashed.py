# Generated by Django 3.1.3 on 2021-04-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='id_hashed',
            field=models.CharField(max_length=16, null=True),
        ),
    ]