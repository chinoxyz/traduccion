
import urllib

from django.conf import settings
from django.core.mail import send_mail

from backend.components.mailsystems.sendemailbase import SendEmailBase


class SendGuestInvitation(SendEmailBase):
    @staticmethod
    def sendMail(giver, user, password, message=None):
        email = user.preferred_email
        
        title = "Cocoon Account"
        
        name = giver.first_name+" "+giver.last_name
        
        
        
        message = 'Hello,\n'\
        '{} have invited you to join Cocoon as a Guest to admin his/her account.'\
        'The credentials of your account are the following:\n'\
        'user: {}\n'\
        'password:{}\n'\
        'In order to access your account, you must download the CocoonApp through the AppStore.\n'\
        'Remember to update your profile!\n'\
        '\n'\
        'Cocoon Team\n'\
        ''.format(name, email, password)
        
        
        return SendGuestInvitation.send(title, message, SendGuestInvitation.MAILFROM, [email], "Send guest invitation", giver.id)
        
