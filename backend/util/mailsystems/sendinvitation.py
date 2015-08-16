import urllib

from django.conf import settings
from django.core.mail import send_mail

from backend.components.mailsystems.sendemailbase import SendEmailBase


class SendInvitation(SendEmailBase):
    @staticmethod
    def sendMail(owner, user, password, message=None):
        email = user.preferred_email
        
        title = "Cocoon Account"
        
        name = owner.first_name+" "+owner.last_name
        
        
        
        message = 'Hello,\n'\
        '{} have invited you to join Cocoon Team by creating you an account.'\
        'The credentials of your account are the following:\n'\
        'user: {}\n'\
        'password:{}\n'\
        'In order to access your account, you must download the CocoonApp through the AppStore.\n'\
        'Remember to update your profile!\n'\
        '\n'\
        'Cocoon Team\n'\
        ''.format(name, email, password)
        
        
        return SendInvitation.send(title, message, SendInvitation.MAILFROM, [email], "Send Invitation", owner.id)
        
