# Generated by Django 3.1.3 on 2021-04-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BooleanField(null=True),
        ),
    ]
