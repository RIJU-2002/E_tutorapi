# Generated by Django 4.1.3 on 2023-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Qualification',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
