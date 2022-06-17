from rest_framework import serializers
from .models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserModelSerializer0and2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_superuser', 'is_staff')

class UserModelSerializer0and3(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_active', 'birthday')