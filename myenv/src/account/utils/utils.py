import random
from django.core.mail import send_mail
import socket

def generate_random_code(length):
    resp = str(random.randint(100000, 999999))
    
    return resp[:length]


def send_otp_email(senderEmail, recipientEmail, otp, userID):
    subject = f'OTP Code verification'.upper()
    message = f'OTP code is: {otp}. Permit user {userID} to signup against your company by giving OTP code to user'
    from_email = f'{senderEmail}'  # Replace with your email or let server use defaul email in the settings 
    recipient_list = [recipientEmail]
    
    
    try:
        email_resp = send_mail(subject, message, from_email, recipient_list)
        return email_resp
    
    except socket.gaierror as error:
        if str(error).endswith("failed"):
            return False
