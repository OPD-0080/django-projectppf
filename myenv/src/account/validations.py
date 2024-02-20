import re

def validate_registration(request):
    context = {}
    
    print("validating registration fields...")
    
    if request.data["email"] == "" or request.data["email"] == None:
        context = {
            "msg": "Error. Provide Email !",
            "status": False
        }
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', request.data["email"]):
        context = {
            "msg": "Error. Provide Valid Email !",
            "status": False
        }
    elif request.data["businessName"] == "" or request.data["businessName"] == None:
        context = {
            "msg": "Error. Provide Your Business Name !",
            "status": False
        }
    elif request.data["natureOfBusiness"] == "" or request.data["natureOfBusiness"] == None:
        context = {
            "msg": "Error. Provide Your Nature of Business !",
            "status": False
        }
    elif request.data["businessType"] == "" or request.data["businessType"] == None:
        context = {
            "msg": "Error. Provide your Business Type !",
            "status": False
        }
    elif request.data["location"] == "" or request.data["location"] == None:
        context = {
            "msg": "Error. Provide your Location !",
            "status": False
        }
    elif request.data["contact"] == "" or request.data["contact"] == None:
        context = {
            "msg": "Error. Provide Your Contact Number !",
            "status": False
        }
    elif request.data["country"] == "" or request.data["country"] == None:
        context = {
            "msg": "Error. Provide Your Country !",
            "status": False
        }
    elif request.data["regionState"] == "" or request.data["regionState"] == None:
        context = {
            "msg": "Error. Provide Your Region / State !",
            "status": False
        }
    elif request.data["town"] == "" or request.data["town"] == None:
        context = {
            "msg": "Error. Provide Your Town !",
            "status": False
        }
    else:
        context = { 
            "msg": "validation complete",
            "status": True
        }
    
    print("Error message from Registration validations ::", context)
    
    if context["msg"]:
        return context
    else:
        return context