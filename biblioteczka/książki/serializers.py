from rest_framework import serializers
from .models import Książka

class KsiążkaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Książka.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    # wykorzystania przy żądaniach
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate_name(self, value):
        temp_value = value.strip().replace(' ', '')
        if not temp_value.isalpha():
            raise serializers.ValidationError(
                "Nazwa musi zawierać tylko litery.!",
            )
        return value

    def validate_description(self, value):
        temp_value = value.strip().replace(' ', '')
        if not temp_value.isalpha():
            raise serializers.ValidationError(
                "Opis musi zawierać tylko litery.!",
            )
        return value

