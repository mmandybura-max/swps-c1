from rest_framework import serializers
from .models import Książka, Autor, Osoba

class KsiążkaSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    tytuł = serializers.CharField(required=True)
    notatki = serializers.CharField(required=True)

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Książka.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    # wykorzystania przy żądaniach
    def update(self, instance, validated_data):
        instance.tytuł = validated_data.get('tyuł', instance.tytuł)
        instance.notatki = validated_data.get('notatki', instance.notatki)
        instance.save()
        return instance

    def validate_tytuł(self, value):
        temp_value = value.strip().replace(' ', '')
        if not temp_value.isalpha():
            raise serializers.ValidationError(
                "Nazwa musi zawierać tylko litery.!",
            )
        return value

    def validate_notatki(self, value):
        temp_value = value.strip().replace(' ', '')
        if not temp_value.isalpha():
            raise serializers.ValidationError(
                "Opis musi zawierać tylko litery.!",
            )
        return value

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'
        # fields = ['id', 'tytuł', 'autor', 'autor_id', 'isbn', 'jakość', 'stan', ]

    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(),
        source='autor',
        write_only=True
    )
