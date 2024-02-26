from rest_framework import serializers

from .models import RegistrationModel, UserModel


class SerializeRegistration(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = ("email", "businessName", "natureOfBusiness", "businessType",
                    "location", "address", "contact", "businessLogo", "country", "regionState", "town", "ceo")
        
class SerializeSignup(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", "first_name", "last_name", "contact_number", "company", "department", "newPass", "confirmPass",)
        