# Generated by Django 2.1 on 2019-03-15 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20190315_0827'),
        ('idc', '0008_auto_20190315_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='uposition',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='u_server', to='server.Server', verbose_name='服务器'),
        ),
    ]
