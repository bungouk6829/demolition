# Generated by Django 2.2.4 on 2020-11-20 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_notice_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice_post',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_10',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_7',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_8',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notice_post',
            name='image_9',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Notice_post_file',
        ),
    ]