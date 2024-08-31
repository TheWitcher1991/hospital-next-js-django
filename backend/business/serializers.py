from rest_framework import serializers


class YookassaWebhookSerializer(serializers.Serializer):
    type = serializers.CharField()
    event = serializers.CharField()
    object = serializers.DictField()
