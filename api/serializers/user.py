from rest_framework import serializers
from user.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}  # To ensure password isn't returned in responses

    def create(self, validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user