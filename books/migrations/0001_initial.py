# Generated by Django 3.0.6 on 2020-05-21 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('bookID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='图书编号')),
                ('bookName', models.CharField(max_length=64, verbose_name='图书名称')),
                ('bookPublishTime', models.DateField(blank=True, null=True, verbose_name='发布时间')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('hID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='图书编号')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=200)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookInfo')),
            ],
            options={
                'verbose_name': '人物',
                'verbose_name_plural': '人物',
            },
        ),
    ]
