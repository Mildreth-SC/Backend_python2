from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings

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

def diagnostics(request):
    return JsonResponse({
        'host': request.get_host(),
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'debug': settings.DEBUG,
        'headers': dict(request.headers),
    })

urlpatterns = [
    path('', home, name='home'),
    path('diagnostics/', diagnostics, name='diagnostics'),
    path('admin/', admin.site.urls),
    path('api/', include('empleados.urls')),
]
