from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type':
                                                                 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type':
                                                                         'password'})

    class Meta:
        model = MyUser
        fields = (
            'email', 'name', 'number', 'organisations', 'city', 'pincode',
            'address', 'password', 'confirm_password')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = MyUser.objects.create_user(**validated_data)
        return user
