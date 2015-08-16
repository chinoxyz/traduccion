import logging

from django.conf import settings
from django.core.mail import send_mail

from backend.components.util import strformat
from django.template.context import Context
from django.template.loader import get_template

logger = logging.getLogger(__name__)

class SendEmailBase():
	MAILFROM = 'Cocoon Team <support@cocoonapp.com>' #"error@corporatecocoon.com"
	#
	@staticmethod
	def constructHTML(message=""):
		template = get_template('emailbase.html')
		context = Context({'body': message})
		content = template.render(context)
		return content
	
	
	@staticmethod
	def send(title, message, emailfrom, emailtoList, loggerInfo = "", userID=None, html_message = None):
		"""
		Send a message to the emailtoList.
		LoggerInfo is the message for logger and UserID is the user responsible for sending the email.
		"""
		if(settings.TEST_MODE):
			return True
		try:
			send_mail(title, message, emailfrom, emailtoList, fail_silently=False, html_message = html_message)
			logger.info(strformat("Email sending: ",loggerInfo," EmailList:",emailtoList," User:",userID))
		except Exception as e:
			logger.warning(strformat("Email failed sending: ",loggerInfo," EmailList:",emailtoList," User:",userID, "Exception ",str(e))) 
			return False
		return True
	
	
	