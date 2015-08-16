


import urllib

from django.conf import settings
from django.core.mail import send_mail

from backend.components.mailsystems.sendemailbase import SendEmailBase
import logging
logger = logging.getLogger(__name__)


class ConfirmEmail(SendEmailBase):
    @staticmethod
    def sendMail(userEmailOBJ, code):
        email = userEmailOBJ.email
        
        title = "Cocoon Account"
        
        name = userEmailOBJ.user.first_name+" "+userEmailOBJ.user.last_name
        link = settings.DOMAIN+'views/validateemail?'+urllib.urlencode({'code':code})
        linkunsubscribe = settings.DOMAIN+'views/unsubscribe?'+urllib.urlencode({'code':code})
        message = 'Hello {},\n\n'\
        'Your email {} has been registered in CocoonApp.com. Please follow this link to confirm your e-mail address:\n'\
        '\n'\
        '{}\n'\
        '\n'\
        'Thanks,\n'\
        'Cocoon Team\n'\
        '\n'\
        '\n'\
        'If you do not recognize this message please follow this link:\n'\
        '\n'\
        '{}\n'.format(name, email, link, linkunsubscribe)
        
        html_message = ConfirmEmail.constructHTML(message)
        
        return ConfirmEmail.send(title, message, ConfirmEmail.MAILFROM, [email], "Email Confirmation",userEmailOBJ.user.id,html_message)