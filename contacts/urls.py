from django.urls import path
from .views import UserApiView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('api-register/', UserApiView.as_view()),
    # JWT Token authentication
    path('api-token/', jwt_views.TokenObtainPairView.as_view()),
    path('api-token-refresh/', jwt_views.TokenRefreshView.as_view()),



]
