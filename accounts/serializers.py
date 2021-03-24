from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class CMSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "is_staff",
            "is_superuser",
            "is_active"
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "phone_number": {"required": True},
        }
        
    def validate_password(self, password):
        validate_password(password=password, user=None)
        return password
    
    def create(self, validated_data, *args, **kwargs):
        password = validated_data.pop("password")
        instance = super(CMSUserSerializer, self).create(validated_data, *args, **kwargs)
        instance.set_password(password)
        instance.save()
        return instance
