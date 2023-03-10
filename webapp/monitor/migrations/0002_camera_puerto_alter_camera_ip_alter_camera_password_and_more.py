# Generated by Django 4.1.3 on 2022-12-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="camera",
            name="puerto",
            field=models.IntegerField(default=0, verbose_name="Puerto"),
        ),
        migrations.AlterField(
            model_name="camera",
            name="ip",
            field=models.CharField(max_length=50, verbose_name="Ip"),
        ),
        migrations.AlterField(
            model_name="camera",
            name="password",
            field=models.CharField(max_length=200, verbose_name="Password"),
        ),
        migrations.AlterField(
            model_name="camera",
            name="usuario",
            field=models.CharField(max_length=200, verbose_name="Usuario"),
        ),
    ]
