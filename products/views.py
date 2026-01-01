from rest_framework import viewsets
from rest_framework.response import Response
from .models import product
from .serializers import productSerializer

class productViewSet(viewsets.ViewSet):

    def list(self, request):

        products = product.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = productSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response(productSerializer(product).data)