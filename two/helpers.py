import socket
from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_mail(email,token):
    subject = 'Your password reset link'
    reset_link = f'http://127.0.0.1:8000/change-password/{token}/'
    message = f'Hi,\n\nClick on the link below to reset your password:\n\n{reset_link}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    try:
        socket.gethostbyname(settings.EMAIL_HOST)        
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"An error occurred while sending email: {e}")
        return False
  