# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import BookInfo
from .models import HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = "__all__"


class HeroInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroInfo
        fields = "__all__"








