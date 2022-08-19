from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

# router = routers.DefaultRouter()
# router.register(r'Product', ProductViewSet)
from shop_api.views import ProductApiList, ProductApiUpdate, ProductApiDetailView, CatApiList, OrderApiList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categ/', CatApiList.as_view()),
    path('api/v1/product/', ProductApiList.as_view()),
    path('api/v1/product/<int:pk>/', ProductApiUpdate.as_view()),
    path('api/v1/prod_detail/<int:pk>/', ProductApiDetailView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/token /', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/cart', OrderApiList.as_view())
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
