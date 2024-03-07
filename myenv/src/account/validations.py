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
    elif request.data["ceo"] == "" or request.data["ceo"] == None:
        context = {
            "msg": "Error. Provide Your Full name as CEO !",
            "status": False
        }
    elif request.data["newPass"] == "" or request.data["newPass"] == None:
        context = {
            "msg": "Error. Provide New Password !",
            "status": False
        }
    elif request.data["confirmPass"] == "" or request.data["confirmPass"] == None:
        context = {
            "msg": "Error. Provide Confirm Password !",
            "status": False
        }
    elif request.data["newPass"] != request.data["confirmPass"]:
        context = {
            "msg": "Error. Passwords does not matches !",
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
    
def validate_signup(request):
    print("validating signup fields")
    context = {}
    
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', request.data["email"]):
        context = {
            "msg": "Error. Provide Email !",
            "status": False
        }
    elif request.data["first_name"] == "" or request.data["first_name"] == None:
        context = {
            "msg": "Error. Provide First Name !",
            "status": False
        }
    elif request.data["last_name"] == "" or request.data["last_name"] == None:
        context = {
            "msg": "Error. Provide Last Name !",
            "status": False
        }
    elif request.data["contact_number"] == "" or request.data["contact_number"] == None:
        context = {
            "msg": "Error. Provide Your Contact Number !",
            "status": False
        }
    elif request.data["company"] == "" or request.data["company"] == None:
        context = {
            "msg": "Error. Provide Your Company !",
            "status": False
        }
    elif request.data["department"] == "" or request.data["department"] == None:
        context = {
            "msg": "Error. Provide Your Department !",
            "status": False
        }
    elif request.data["newPass"] == "" or request.data["newPass"] == None:
        context = {
            "msg": "Error. Provide New Password !",
            "status": False
        }
    elif request.data["confirmPass"] == "" or request.data["confirmPass"] == None:
        context = {
            "msg": "Error. Provide Confirm Password !",
            "status": False
        }
    elif request.data["newPass"] != request.data["confirmPass"]:
        context = {
            "msg": "Error. Password does not matches !",
            "status": False
        }
    else:
        context = { 
            "msg": "validation complete",
            "status": True
        }
    print("Error message from Signup validations ::", context)
    
    if context["msg"]:
        return context
    else:
        return context
    
def validate_otp(request):
    print("validating OTP fields")
    context = {}
    
    if request.data["otp"] == "" or request.data["otp"] == None:
        context = {
            "msg": "Error. Provide valid OTP code !",
            "status": False
        }
    else:
        context = { 
            "msg": "validation complete",
            "status": True
        }
    
    print("Error message from Signup validations ::", context)
    
    if context["msg"]:
        return context
    else:
        return context