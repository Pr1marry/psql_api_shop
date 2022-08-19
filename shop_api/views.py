from rest_framework import generics, mixins
# from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Product, Category, Bin
from .serializers import ProductSerializer, CatSerializer, CartSerializer


class CatApiList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class ProductApiList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ProductApiUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser, )


class ProductApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser, )


class OrderApiList(generics.ListCreateAPIView):
    queryset = Bin.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser, )

# class ProductViewSet(mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      mixins.ListModelMixin,
#                      GenericViewSet):
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

