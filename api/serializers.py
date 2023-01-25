from rest_framework import serializers
from todo.models import Todo

# Create a TODO model Serialzer

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created', 'completed']
    