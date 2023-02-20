from pkg_resources import require
from rest_framework import serializers
from api.models import CheckBox

class CheckBoxSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = CheckBox
        fields = ['name', 'is_checked', 'title']
    @staticmethod
    
    def get_title(obj):
        return obj.name + " " + "python"

class DataSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    attrs = serializers.JSONField(required=False)
    type = serializers.CharField(required=False)
    val_1 = serializers.IntegerField()
    val_2 = serializers.IntegerField()


    @staticmethod
    def validate_type(type):
        if type not in ['dict', 'list', 'tuple']:
            raise serializers.ValidationError('Invalid type')
        return type
