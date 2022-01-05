from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from auction.api.user.models import DeliveryInfo


class SellerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='seller.name')
    address = serializers.CharField(source='seller.address')

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'address')


class DeliveryInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryInfo
        fields = ('name', 'address', 'phone')
