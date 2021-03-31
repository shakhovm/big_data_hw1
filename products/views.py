from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from products.serializers import ProductDetailSerializer
from reviews.serializers import ReviewDetailSerializer
from products.models import Product
from reviews.models import Review
from reviews.serializers import ReviewDetailSerializer
# Create your views here.
#
# class ProductReviewView(generics.ListAPIView):
#     serializer_class = ReviewDetailSerializer
#     queryset = Review.objects.raw("""
#             SELECT * FROM reviews_review WHERE product_id = %s
#             """, pk)


class ProductReviewView(APIView):
    def get(self, request, pk):
        review = Review.objects.filter(product_id=pk)
        return Response(ReviewDetailSerializer(review, many=True).data)


class ProductReviewStarRatingView(APIView):
    def get(self, request, pk, star_rating):
        review = Review.objects.filter(product_id=pk, star_rating=star_rating)
        return Response(ReviewDetailSerializer(review, many=True).data)

