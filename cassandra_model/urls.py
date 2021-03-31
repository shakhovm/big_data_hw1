from django.urls import path, include
from cassandra_model.views import *


app_name = 'cassandra'
urlpatterns = [
    path('review_by_product/<str:product_id>/', ReviewByProductView.as_view()),
    path('review_by_customer/<int:customer_id>/', ReviewByCustomerView.as_view()),
    path('review_by_product/<str:product_id>/<int:star_rating>/',
         ReviewByProductStarRatingView.as_view()),
    path('most_reviewed_items/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostReviewedItemsView.as_view()),
    path('most_productive_customers/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveCustomersView.as_view()),
    path('most_productive_backers/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveBackersView.as_view()),
    path('most_productive_haters/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveHatersView.as_view())
]