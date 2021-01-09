from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
