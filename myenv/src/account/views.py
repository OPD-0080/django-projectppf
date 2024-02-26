## IMPORTATION OF MODULES
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
import json



# Create your views here.
@api_view(["GET"])
def registration(request):
    context = {}
    print("Inside Registration router")
    
    
    
    
    return Response(context, status=status.HTTP_200_OK)



@api_view(["GET"])
def signup(request):
    context = {}
    print("Inside Singup router")
    
    
    
    
    return Response(context, status=status.HTTP_200_OK)


@api_view(["GET"])
def page_not_found(request):
    context = {}
    print("Inside 404 router")
    
    
    
    
    return Response(context, status=status.HTTP_200_OK)


@api_view(["GET"])
def internal_server_error(request):
    context = {}
    print("Inside 500 router")
    
    
    
    
    return Response(context, status=status.HTTP_200_OK)