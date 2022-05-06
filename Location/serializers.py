from urllib import response
from rest_framework import serializers
from .models import Street, Area


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

# function for soft deletion

    def destroy(self, request, *args, **kwargs):
        street = self.get_object()
        street.is_active = False
        street.save()
        return response(data='delete success')


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'url', 'name')
