from os import name
from django.urls import path
from .views import (ReviewList, ReviewDetail, ReviewCreate,
                    WatchDetailAv, WatchListAv, 
                    StreamPlatformAv, StreamPlatformDetailAv)
# from watchlist_app.api.views import movie_details, movie_list, movie_details

urlpatterns = [    
    path('list/', WatchListAv.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAv.as_view(), name='watch-detail'),
    path('stream/', StreamPlatformAv.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAv.as_view(), name='streamplatform-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]

