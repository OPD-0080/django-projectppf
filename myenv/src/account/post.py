## IMPORTATION OF MODULES
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
import json
from django.contrib.auth import authenticate
import socket

## ....
## IMPORTATION OF FILES
from .models import RegistrationModel, UserModel
from .validations import validate_registration, validate_signup, validate_otp
from .serializers import SerializeRegistration, SerializeSignup, SerializeOTPCodes
from .utils.utils import generate_random_code, send_otp_email
## ...


@api_view(["POST"])
@permission_classes([AllowAny])
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


@api_view(["POST"])
@permission_classes([AllowAny])  # Allowing all user to have access to the endpoint without any restriction 
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
    userID = f"{company[:3].lower()}{generate_random_code(4)}"
    
    
    ## validate fields 
    validate_resp = validate_signup(request)
    ## ...
    if validate_resp["status"]:
        pass
    else: 
        context = {
            "msg": validate_resp["msg"]
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    ## ....
    ## serializing data after validating fields 
    serializer = SerializeSignup(data= data)
    if serializer.is_valid(raise_exception=False):
        ## chcking if user choice of company already registered in db
        try:
            company_biodata = RegistrationModel.objects.get(businessName= company)
            print("company biodata resp ..", company_biodata)
            pass
        
        except RegistrationModel.DoesNotExist:
            context = {
                "msg": f"Choice of Company {company} does not exist. Register Your Business Now!"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        ## ....
        ## check if user is already signup
        try:
            user = UserModel.objects.get(email= email) ## user already signup
            context = {
                "msg": f"User with {email} already exists. Login !"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
        except UserModel.DoesNotExist: ##  user is singup for the first time against the company 
            new_user = UserModel.objects.create(
                    email= email, first_name= first_name, last_name= last_name, middle_name= middle_name,
                    contact_number= contact_number, company= company, department= department, userID= userID
                )
            new_user.set_password(confirmPass)
            new_user.save()
            Token.objects.create(user= new_user) ## craete a new token for the user after data is stored in db
            
            ##  send OTP code to  company email for verification 
            print("sending OTP code to company for user verification")
            senderEmail = "" ## allowing server to use deafault email in settings 
            recipientEmail = "obengprince0001@gmail.com"
            otp = generate_random_code(4)
            email_resp = send_otp_email(senderEmail= senderEmail, recipientEmail= recipientEmail, otp= otp, userID= userID)
            print("Emailing response ..:", email_resp)

            if email_resp > 0:
                print("OTP code sent sucessfully")
                ## update user sgnup profile  with otp code 
                user = UserModel.objects.get(email= email) 
                user.otp = otp
                user.save()
                ## ...
                
                context = {
                    "msg": f"Contact {company} Admin for OTP Code for verification",
                    "otp_signal": True  ## otp signal for poping out overlay page in signup page to receive OTP code for verification 
                }
                return Response(context, status=status.HTTP_200_OK)
            
            else:
                print("Error in OTP code. Undo changes by deleting user ")
                ## undo changes in db 
                current_user = UserModel.objects.filter(email= email)
                current_user.delete()
                
                context = {
                    "msg": "Network Error. Refresh page & Try Again !",
                    "otp_signal": False ## otp signal to hide overlay page in signup page to receive OTP code for verification 
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            ## ...
        ##
        
    else:
        print("Serializer Error ...:", serializer.errors)
        context = {
            "msg": f"User with {email} already exist.",
            "code": serializer.errors
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def otp_verification(request):
    print("** Inside OTP verification route **")
    
    data = json.loads(request.body)
    otp = data.get("otp", None)
    
    print("collecting data for OPT verification ...:", data)
    
    ## validating input fields
    validate_resp = validate_otp(request) 
    if validate_resp["status"]:
        pass
    else:
        context = {
            "msg": validate_resp["msg"]
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    ## ....
    ## serializing data after validating fields
    serializer = SerializeOTPCodes(data=data, many=False)
    if serializer.is_valid():
        print("getting seriliazer data ...:", serializer)
        
        ## crosschck if OTP provided matches with the OTP codde in db
        
        
        
        
        
    else:
        print("Serializer Error ...:", serializer.errors)
        context = {
            ##"msg": f"User with {email} already exist.",
            "code": serializer.errors
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    