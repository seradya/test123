from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ClientForm
from .models import Service


def main(request):
    return render(request, 'main/index.html')

def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # name = request.POST['name']
            # email = request.POST['email']
            # subject = 'Новый клиент'
            # message = 'Имя: ' + name + ' | email: ' + email
            # sender = ''
            # recipient = ''
            # send_mail(subject, message, sender, [recipient], fail_silently=False)
            return JsonResponse({"result":"Ура!"})
        else:
            return JsonResponse({"result":"Плохо"})

def services(request):
    goods = Service.objects.filter(is_active=True)
    context = {
        'goods': goods
    }
    return render(request, 'main/services.html', context)