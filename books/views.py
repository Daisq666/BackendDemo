# -*- coding: utf-8 -*-

from django.shortcuts import render

from books import models
from books import serializers
from rest_framework import viewsets

# Create your views here.


class BookInfoViewSet(viewsets.ModelViewSet):
    queryset = models.BookInfo.objects.all()
    serializer_class = serializers.BookInfoSerializer


class HeroInfoViewSet(viewsets.ModelViewSet):
    queryset = models.HeroInfo.objects.all()
    serializer_class = serializers.HeroInfoSerializer