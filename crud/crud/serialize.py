from rest_framework import serializers
from crud.models import DetailsModel

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= DetailsModel
        fields="__all__"