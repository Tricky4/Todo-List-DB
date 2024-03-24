from rest_framework import serializers
from todo_app.models import (TaskList, Category)

class TaskListSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = TaskList
        fields = '__all__'
        
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None    
        
    def create(self, validated_data):
        category_name = validated_data.pop('category_name', None)
        if category_name:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                raise serializers.ValidationError("Invalid category name.")

            validated_data['category'] = category

        return super().create(validated_data)
        
class CategorySerializer(serializers.ModelSerializer):
    tasklist = TaskListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'