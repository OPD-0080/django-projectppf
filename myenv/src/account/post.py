## IMPORTATION OF MODULES
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
import json

## ....
## IMPORTATION OF FILES
from .models import RegistrationModel, UserModel
from .validations import validate_registration, validate_signup
from .serializers import SerializeRegistration, SerializeSignup
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
    ceo = data.get("ceo", None)
    role = data.get("role", None)
    confirmPass = data.get("confirmPass", None)

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
                        businessLogo= businessLogo, country= country, regionState= regionState, town= town,
                        ceo= ceo, role= role
                    )
                new_biodata.set_password(confirmPass)
                new_biodata.save()
                ##Token.objects.create(user= new_biodata) ## create nwe token for the user
                context = {
                    "msg": f"{businessName} Registered Sucessful"
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
    
    data = json.loads(request.body)
    print(f"Collecting data from signup UI ::", data)
    
    ## destructuring data
    email = data.get("email", None)
    first_name = data.get("first_name", None)
    last_name = data.get("last_name", None)
    middle_name = data.get("middle_name", None)
    contact_number = data.get("contact_number", None)
    company = data.get("company", None)
    department = data.get("department", None)
    confirmPass = data.get("confirmPass", None)
    
    
    ## validate fields 
    validate_resp = validate_signup(request)
    ## ...
    if validate_resp["status"]:
        ## serializing data after validating fields 
        serializer = SerializeSignup(data= data)
        if serializer.is_valid(raise_exception=False):
            # check if user is already signup
            try:
                user = UserModel.objects.get(email= email) ## user already signup
                context = {
                    "msg": f"User with {email} already signup"
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            except UserModel.DoesNotExist: ##  user is singup for the first time
                new_user = UserModel.objects.create(
                        email= email, first_name= first_name, last_name= last_name, middle_name= middle_name,
                        contact_number= contact_number, company= company, department= department
                    )
                new_user.set_password(confirmPass)
                new_user.save()
                Token.objects.get_or_create(user= new_user) ## craete a new token for the user after data is stored in db
                
                ##  send OTP code to  company email for verification 
                try:
                    biodata = RegistrationModel.objects.get(businessName= company)
                    
                    
                    
                    
                except  RegistrationModel.DoesNotExist:
                    context = {
                        "msg": f"{company} biodata does not exist. Register Now !"
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
                ## ...
            ##
        else:
            print("Serializer Error ...:", serializer.errors)
            context = {
                "msg": "",
                "code": serializer.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else: 
        context = {
            "msg": validate_resp["msg"]
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)