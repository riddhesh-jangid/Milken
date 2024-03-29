# Generated by Django 2.0.7 on 2019-01-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0010_auto_20190102_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='money',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='money',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='last_payment',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='remaining',
            field=models.FloatField(default=0.0),
        ),
    ]
