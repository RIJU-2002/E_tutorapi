# Generated by Django 4.1.3 on 2023-04-27 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_latitude_alter_user_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='user',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subjects',
        ),
    ]
