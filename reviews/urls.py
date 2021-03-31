from django.urls import path, include
from reviews.views import *


app_name = 'reviews'
urlpatterns = [
    path('review_by_customer/<int:pk>/', ReviewByCustomer.as_view()),
    path('most_reviewed_items/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostReviewedItemsView.as_view()),
    path('most_productive_customers/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveCustomers.as_view()),
    path('most_productive_backers/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveBackers.as_view()),
    path('most_productive_haters/<str:first_date>/<str:second_date>/<int:number_of_products>/',
         MostProductiveHaters.as_view())
]