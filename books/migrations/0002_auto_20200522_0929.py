# Generated by Django 3.0.6 on 2020-05-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.CharField(choices=[('B', '男'), ('G', '女')], default='B', max_length=1, verbose_name='英雄性别'),
        ),
    ]