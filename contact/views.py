from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # print(f'Tipo de petición: {request.method}')
    contact_form=ContactForm() #Instanciando una clase form
    if request.method == 'POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            affair=request.POST.get('affair','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')

            #estructura del mensaje
            email=EmailMessage(
                f'{affair}',
                f'{name} <{email}> \n\n Dijo: \n\n {message}',
                f'{email}',
                ['rincondelcaballero@info.com'],
                reply_to=[email],
            )

            #Enviar el correo
            try:
                email.send()
                return redirect(reverse('contact')+'?OK')
            except:
                return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html', {'contact_form':contact_form})