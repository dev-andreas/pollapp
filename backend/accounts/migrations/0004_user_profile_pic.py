# Generated by Django 3.1.3 on 2021-04-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]