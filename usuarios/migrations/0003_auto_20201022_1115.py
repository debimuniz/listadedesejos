# Generated by Django 3.1.2 on 2020-10-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20201019_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
