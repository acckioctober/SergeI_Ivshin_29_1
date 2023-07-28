from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/genres/', views.genres_list_api_view),
    path('api/v1/directors/', views.directors_list_api_view),
    path('api/v1/movies/', views.movies_list_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/directors/<int:pk>/', views.director_detail_api_view),
    path('api/v1/movies/<int:pk>/', views.movie_detail_api_view),
    path('api/v1/reviews/<int:pk>/', views.review_detail_api_view),
    path('api/v1/movies/reviews/', views.movies_reviews_view),
    ]
