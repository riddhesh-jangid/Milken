# Generated by Django 2.0.7 on 2019-01-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0011_auto_20190113_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='pin',
            field=models.IntegerField(default=0),
        ),
    ]