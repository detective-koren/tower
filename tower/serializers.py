from rest_framework import serializers


from .models import (
    Nuc, Person, DetectedInformation
)


class DetectedInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectedInformation
        exclude = []