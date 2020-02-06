# Generated by Django 2.2.1 on 2019-10-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0023_auto_20191001_1448")]

    operations = [
        migrations.AddField(
            model_name="vmessnode",
            name="grpc_host",
            field=models.CharField(
                default="0.0.0.0", max_length=64, verbose_name="Grpc地址"
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="grpc_port",
            field=models.CharField(
                default="8080", max_length=64, verbose_name="Grpc端口"
            ),
        ),
        migrations.AlterField(
            model_name="usertraffic",
            name="last_use_time",
            field=models.DateTimeField(
                blank=True, db_index=True, verbose_name="上次使用时间"
            ),
        ),
    ]