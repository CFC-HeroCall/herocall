# Generated by Django 3.2.5 on 2021-07-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210723_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post'),
        ),
    ]