from rest_framework import generics
from .models import Empleado
from .Serializer import EmpleadoSerializer

class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'idEmpleado'
