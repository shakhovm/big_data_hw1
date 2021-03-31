from django.urls import path
from products.views import *


app_name = 'products'
urlpatterns = [
    path('review_by_product/<str:pk>/', ProductReviewView.as_view()),
    path('review_by_product/<str:pk>/<int:star_rating>/', ProductReviewStarRatingView.as_view())
]
