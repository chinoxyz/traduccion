


import urllib

from django.conf import settings
from django.core.mail import send_mail
from django.template.context import Context
from django.template.loader import get_template

from backend.components.mailsystems.sendemailbase import SendEmailBase


class ForgotPassword(SendEmailBase):
    @staticmethod
    def sendMail(user, code):
        
        email = user.preferred_email
        
        title = "Cocoon Change Password"
        
        name = user.first_name+" "+user.last_name
        link = settings.DOMAIN+'views/forgotpassword?'+urllib.urlencode({'code':code})
        message = 'Hi {},\n\n'\
        'You have requested to reset your password for CocoonApp.\n\n'\
        'To proceed with your request, please click on the following link to reset it:\n'\
        '{}\n\n'\
        'If you\'re not a CocoonApp user or didn\'t request it, you can ignore this email.'\
        .format(name, link)
        
        html_message = ForgotPassword.constructHTML(message)
        
        
        
        return ForgotPassword.send(title, message, ForgotPassword.MAILFROM, [email], "Forgot password request", user.id, html_message)
        