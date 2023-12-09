from rest_framework import serializers
from .models import Theory


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theory
        fields = ['title', 'sub_title', 'image']
