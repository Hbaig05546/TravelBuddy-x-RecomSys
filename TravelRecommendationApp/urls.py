''' /TravelRecommendationSystem/urls.py '''

from TravelRecommendationApp.views import *
from django.urls import path

urlpatterns = [
    path('recommend_category/',DestinationRecommend_category),
    path('recommend_tags/',DestinationRecommend_tags),
    # path('destination_category_add/',destination_category_add),
]