# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

'''
图书类
'''


class BookInfo(models.Model):
    bookID = models.BigAutoField(primary_key=True, verbose_name=u"图书编号")
    bookName = models.CharField(max_length=64, verbose_name=u"图书名称")
    bookPublishTime = models.DateField(verbose_name="发布时间", null=True, blank=True)
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    class Meta:
        verbose_name = u"图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bookName


#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    HeroSex_CHOICES = (
        ('B', u"男"),
        ('G', u"女"),
    )

    hID = models.BigAutoField(primary_key=True, verbose_name=u"图书编号")
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.CharField(verbose_name=u"英雄性别", default='B', max_length=1,
                                choices=HeroSex_CHOICES)  # 面向宝宝性别（B:男/G:女/N:通用）#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

    class Meta:
        verbose_name = u"人物"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname