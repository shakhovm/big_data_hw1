from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import ProductDetailSerializer
from reviews.serializers import ReviewDetailSerializer, ReviewCustomerSerializer
from reviews.models import Review
from django.db.models import Count


# Create your views here.


class ReviewByCustomer(APIView):
    @staticmethod
    def get(request, pk):
        review = Review.objects.filter(customer_id=pk)
        return Response(ReviewDetailSerializer(review, many=True).data)


class MostReviewedItemsView(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        result = Review.get_most_reviewed_items(first_date,
                                                second_date,
                                                number_of_products)
        return Response(ProductDetailSerializer(result, many=True).data)


class MostProductiveCustomers(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        result = Review.get_productive_customers(first_date,
                                                 second_date,
                                                 number_of_products)
        return Response(result)


class MostProductiveHaters(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        result = Review.get_productive_haters(first_date,
                                              second_date,
                                              number_of_products)
        return Response(result)


class MostProductiveBackers(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        result = Review.get_productive_backers(first_date,
                                               second_date,
                                               number_of_products)
        return Response(result)
