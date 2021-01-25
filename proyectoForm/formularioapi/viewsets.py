from rest_framework import viewsets
from . import models
from . import serializers

class FormularioViewset(viewsets.ModelViewSet):
    queryset = models.Formulario.objects.all()
    serializer_class = serializers.FormularioSerializer


