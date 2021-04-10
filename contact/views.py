from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['bookworms1212@gmail.com'], # To Email
            fail_silently=False,
			)

        return render(request, 'contact/contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact/contact.html', {})
