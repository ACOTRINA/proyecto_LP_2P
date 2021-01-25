from mascotasapi.viewsets import MascotaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mascota', MascotaViewset)

