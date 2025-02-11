from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CategoryListAPIView(ListAPIView):
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


s


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class New(APIView):
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post (self,request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )



class view(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]



class pop(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)





class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(
            serializer.data
        )



