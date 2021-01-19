from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    # list_id = serializers.IntegerField()
    # list_name = serializers.CharField(min_length = 10, max_length = 100, allow_blank = False)

    class Meta:
        model = TodoList
        fields = ['list_name', 'id']
        read_only_fields = ['id']

    # def create(self, validated_data):
    #     return TodoList.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.list_name = validated_data['list_name']
    #     instance.save()
    #     return instance
