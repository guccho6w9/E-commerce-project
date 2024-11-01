from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, User
from django.contrib.auth import authenticate
from .serializers import ProductSerializer
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
# from .utils import scrape_products

# def run_scraper(request):
 #    products = scrape_products()  # Llama a la función para obtener los productos
 #    return render(request, 'your_template.html', {'products': products}) 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def register_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            return Response({
                "message": "Inicio de sesión exitoso",
                "user_id": user.id,
                "name": user.name,  # Usa el campo name directamente
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
