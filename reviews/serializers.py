from rest_framework import serializers
from reviews.models import Review


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCustomerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()