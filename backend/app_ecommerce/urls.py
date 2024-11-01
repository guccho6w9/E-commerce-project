from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, register_user, login_user # run_scraper  # Importa las vistas

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Rutas de la API
    path('register/', register_user, name='register'),  # Ruta de registro con barra al final
    path('login/', login_user, name='login'),  # Ruta de login con barra al final
    # path('scraper/', run_scraper, name='run_scraper'),
]
