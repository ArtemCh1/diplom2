from rest_framework import serializers

from . import models


class GoogleAuth(serializers.Serializer):
    """ Сериализация данных от Google
    """
    email = serializers.EmailField()
    token = serializers.CharField()