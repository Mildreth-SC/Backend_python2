from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'API Backend Python - Django REST Framework',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'empleados': '/api/empleados/'
        }
    })

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('empleados.urls')),
]
