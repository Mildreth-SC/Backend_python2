from django.urls import path
from .views import (
    EmpleadoListCreateView,
    EmpleadoRetrieveUpdateDeleteView
)

urlpatterns = [
    path('empleados/', EmpleadoListCreateView.as_view()),
    path('empleados/<int:idEmpleado>/', EmpleadoRetrieveUpdateDeleteView.as_view()),
]
