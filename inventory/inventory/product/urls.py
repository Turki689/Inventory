from django.urls import path

from .views import ProductAPIView, New,ProductDetail

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('pop/', ProductDetail.as_view(), name='product-list1'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),


]

