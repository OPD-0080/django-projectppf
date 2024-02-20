from rest_framework import serializers

from .models import RegistrationModel


class SerializeRegistration(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = ("email", "businessName", "natureOfBusiness", "businessType",
                    "location", "address", "contact", "businessLogo", "country", "regionState", "town",)
        