# Generated by Django 3.1.3 on 2020-11-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20201113_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice_post',
            name='clicks',
            field=models.IntegerField(default=1),
        ),
    ]
