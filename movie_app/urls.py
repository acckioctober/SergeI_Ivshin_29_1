from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/genres/', views.GenreListCreateApiView.as_view()),
    path('api/v1/genres/<int:id>/', views.GenreRetrieveUpdateDestroyApiView.as_view()),
    path('api/v1/movies/', views.MovieListCreateApiView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieRetrieveUpdateDestroyApiView.as_view()),
    path('api/v1/directors/', views.DirectorListCreateApiView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorRetrieveUpdateDestroyApiView.as_view()),
    path('api/v1/reviews/', views.ReviewListCreateApiView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyApiView.as_view()),
    path('api/v1/movies/reviews/', views.MovieReviewListApiView.as_view()),

    # path('api/v1/genres/', views.genres_list_api_view),
    # path('api/v1/directors/', views.directors_list_api_view),
    # path('api/v1/movies/', views.movies_list_api_view),
    # path('api/v1/reviews/', views.reviews_list_api_view),
    # path('api/v1/directors/<int:pk>/', views.director_detail_api_view),
    # path('api/v1/movies/<int:pk>/', views.movie_detail_api_view),
    # path('api/v1/reviews/<int:pk>/', views.review_detail_api_view),
    # path('api/v1/movies/reviews/', views.movies_reviews_view),
    ]
