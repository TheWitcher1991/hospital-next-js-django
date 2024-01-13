from rest_framework import serializers
from backend.api.models.position import Position, Cabinet, Shift, Schedule


class PositionCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CabinetCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class ShiftCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class ScheduleCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
