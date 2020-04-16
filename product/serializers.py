from rest_framework import serializers
from .models import Product 
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView

class PorductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PorductSerializer

class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = PorductSerializer

