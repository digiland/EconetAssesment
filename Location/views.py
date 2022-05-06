from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics


from .models import Street, Area
from .serializers import StreetSerializer, AreaSerializer


class StreetApiView(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class AreaView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class StreetinArea(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned street to a given area
        by filtering against an `area` query parameter in the URL.
        """
        queryset = Street.objects.all()
        area = self.request.query_params.get('area')
        if area is not None:
            queryset = queryset.filter(area=area)
        return queryset
