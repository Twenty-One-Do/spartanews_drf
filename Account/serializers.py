from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'password2',
            'date_joined',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
        )
        read_only_fields = (
            'id',
            'date_joined',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
        )

    def validate(self, data):
        print(data)
        if "password" in data or "password2" in data:
            raise serializers.ValidationError({"password": "해당 API에서 password는 수정 불가능합니다."})
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance