from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import User, Resume, Student


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'file', 'uploaded_at']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)  # Groups assigned to the user
    user_permissions = PermissionSerializer(many=True, read_only=True)  # User-specific permissions
    resume = ResumeSerializer(read_only=True)  # Resume associated with the user

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone_number', 'groups', 'user_permissions', 'resume'
        ]
        read_only_fields = ['groups', 'user_permissions', 'resume']  # Prevent these from being updated directly


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Use the create_user method to ensure the password is hashed
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'first_name', 'last_name']
