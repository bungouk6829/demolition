# Generated by Django 2.2.4 on 2020-12-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20201204_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_post',
            name='file_1',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='information_post',
            name='file_2',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='information_post',
            name='file_3',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='information_post',
            name='file_4',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='information_post',
            name='file_5',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='file_1',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='file_2',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='file_3',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='file_4',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='file_5',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y%m%d', verbose_name='파일'),
        ),
    ]
