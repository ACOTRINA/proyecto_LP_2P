from formularioapi.viewsets import FormularioViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('formulario', FormularioViewset)


