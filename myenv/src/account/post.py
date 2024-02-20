## IMPORTATION OF MODULES
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
import json

## ....
## IMPORTATION OF FILES
from .models import RegistrationModel
from .validations import validate_registration
from .serializers import SerializeRegistration
## ...


@api_view(["POST"])
def register(request):
    context = {},
    print("** Inside Register route **")
    data = json.loads(request.body) ## load data from server as dict to JSON format
    
    ## collecting data from UI
    email = data.get("email", None)
    businessName = data.get("businessName", None)
    natureOfBusiness = data.get("natureOfBusiness", None)
    businessType = data.get("businessType", None)
    location = data.get("location", None)
    address = data.get("address", None)
    contact = data.get("contact", None)
    businessLogo = data.get("businessLogo", None)
    country = data.get("country", None)
    regionState = data.get("regionState", None)
    town = data.get("town", None)

    ##  validate input fields
    validation_status = validate_registration(request)
    if validation_status["status"]:
        ## Serializing data 
        serializer = SerializeRegistration(data=data, many=False)   
        if serializer.is_valid(raise_exception=False):
            print("getting serializer data ::", serializer.data)
            
            ## checking fro duplicate of data in db
            try:
                user = RegistrationModel.objects.get(email= email, businessName= businessName)
                context = {
                    "msg": f"{businessName} biodata already exists",
                    "queryResp": user
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            except RegistrationModel.DoesNotExist:
                ## create company biodata 
                new_biodata = RegistrationModel.objects.create(
                        email= email, businessName= businessName, natureOfBusiness= natureOfBusiness,
                        businessType= businessType, location= location, address= address, contact= contact,
                        businessLogo= businessLogo, country= country, regionState= regionState, town= town
                    )
                new_biodata.save()
                context = {
                    "msg": f"{businessName} biodata created sucessfully"
                }
                return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                "msg": f"{businessName} biodata already exists", 
                "code": serializer.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
    else: 
        context = {
            "msg": validation_status["msg"]
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    ## ....


def signup(request):
    context = {}
    print("** Inside Signup route **")
    
    
    
    return Response(context, status=status.HTTP_201_CREATED)