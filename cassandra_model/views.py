from rest_framework.response import Response
from rest_framework.views import APIView
from cassandra_model.serializers import review_serialize
# Create your views here.
from .models import ReviewByCustomer, ReviewByProduct
from .reviewed_items_models import ReviewedItems, CustomerItems


class ReviewByProductView(APIView):
    @staticmethod
    def get(request, product_id):
        res = ReviewByProduct.get_review_by_product(product_id)
        return Response(review_serialize(res))


class ReviewByProductStarRatingView(APIView):
    @staticmethod
    def get(request, product_id, star_rating):
        res = ReviewByProduct.get_review_by_product_star_rating(product_id,
                                                                star_rating)
        return Response(review_serialize(res))


class ReviewByCustomerView(APIView):
    @staticmethod
    def get(request, customer_id):
        res = ReviewByCustomer.get_review_by_customer(customer_id)
        return Response(review_serialize(res))


class MostReviewedItemsView(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        res = ReviewedItems.most_reviewed_items(first_date, second_date,
                                                number_of_products)
        return Response(res)


class MostProductiveCustomersView(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        res = CustomerItems.most_productive_customers(first_date, second_date,
                                                      number_of_products)
        return Response(res)


class MostProductiveHatersView(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        res = CustomerItems.most_productive_haters(first_date, second_date,
                                                   number_of_products)
        return Response(res)


class MostProductiveBackersView(APIView):
    @staticmethod
    def get(request, first_date, second_date, number_of_products):
        res = CustomerItems.most_productive_backers(first_date, second_date,
                                                    number_of_products)
        return Response(res)
