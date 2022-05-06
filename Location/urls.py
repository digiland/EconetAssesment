from django.urls import path, include, re_path
from rest_framework import routers
from .views import (
    StreetApiView, AreaView, StreetinArea
)


router = routers.DefaultRouter()
router.register('streets', StreetApiView)
router.register('area', AreaView)

urlpatterns = [
    path('', include(router.urls)),
    path("<str:area>/", StreetinArea.as_view(), name="streets_in_area"),
]
