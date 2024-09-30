from rest_framework import serializers

from .models import Agent, Face, Division


class DivisionSerialize(serializers.ModelSerializer):
    """
    Сериалайзер дял подразделения агента.
    """

    class Meta:
        model = Division
        fields = ('id', 'name', 'created_at')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)


class FaceSerializer(serializers.ModelSerializer):
    """
    Сериалайзер антиагента.
    """

    class Meta:
        model = Face
        fields = ('id', 'counterparty_type', 'first_name', 'second_name', 'last_name', 'data_birth',
                  'name_legal_entity', 'inn', 'created_at')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)


class AgentSerializer(serializers.ModelSerializer):
    """
    Сериалайзер агента.
    """

    face = serializers.PrimaryKeyRelatedField(queryset=Face.objects.all(), label='Контрагент ')
    division = serializers.PrimaryKeyRelatedField(queryset=Division.objects.all(), label='Подразделение ')

    class Meta:
        model = Agent
        fields = ('id', 'face', 'division', 'status', 'created_at', 'date_begin', 'date_end')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['face'] = FaceSerializer(instance.face).data
        response['division'] = DivisionSerialize(instance.division).data

        return response