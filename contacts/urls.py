from django.urls import path, include
from .views import UserApiView, ContactApiView
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
'''
swagger scheme 
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


'''
end of it 
'''
router = DefaultRouter()
router.register('contacts', ContactApiView)

urlpatterns = [
    path('api-register/', UserApiView.as_view()),
    # JWT Token authentication
    path('api-token/', jwt_views.TokenObtainPairView.as_view()),
    path('api-token-refresh/', jwt_views.TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('scheme/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
