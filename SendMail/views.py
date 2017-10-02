from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from MailProject import settings

def index(request):
	return HttpResponse("This is demo project for sending mails in django.")

def send_email(request):
	context_data = {
		'subject': 'Sent from django',
		'name': 'Harshveer Singh',
		'sender': 'Django Server'
	}
	subject_t = loader.get_template('email_subject.html')
	subject = subject_t.render(context_data)
	body_t = loader.get_template('email_body.html')
	body = body_t.render(context_data)
	
	try:
		send_mail(subject, body, settings.SERVER_EMAIL, ['harshveer1889@gmail.com'], fail_silently=False,)
	except:
		return HttpResponse("Failed to send email.")

	return HttpResponse("Email sent successfully.")