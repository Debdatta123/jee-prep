# Generated by Django 2.2.7 on 2020-11-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='Qid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
