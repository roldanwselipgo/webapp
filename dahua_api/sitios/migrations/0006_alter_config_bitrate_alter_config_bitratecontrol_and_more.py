# Generated by Django 4.1.4 on 2023-01-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0005_remove_config_typestream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='BitRate',
            field=models.IntegerField(blank=True, default=512, null=True, verbose_name='BitRate'),
        ),
        migrations.AlterField(
            model_name='config',
            name='BitRateControl',
            field=models.CharField(blank=True, default='VBR', max_length=100, null=True, verbose_name='BitRateControl'),
        ),
        migrations.AlterField(
            model_name='config',
            name='Compression',
            field=models.CharField(blank=True, default='H.264', max_length=100, null=True, verbose_name='Compression'),
        ),
        migrations.AlterField(
            model_name='config',
            name='CustomResolutionName',
            field=models.CharField(blank=True, default='720p', max_length=100, null=True, verbose_name='Resolution'),
        ),
        migrations.AlterField(
            model_name='config',
            name='FPS',
            field=models.IntegerField(blank=True, default=4, null=True, verbose_name='FPS'),
        ),
        migrations.AlterField(
            model_name='config',
            name='Language',
            field=models.CharField(blank=True, default='English', max_length=100, null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='config',
            name='Quality',
            field=models.IntegerField(blank=True, default=4, null=True, verbose_name='Quality'),
        ),
        migrations.AlterField(
            model_name='config',
            name='SmartCodec',
            field=models.CharField(blank=True, default='Off', max_length=100, null=True, verbose_name='SmartCodec'),
        ),
    ]