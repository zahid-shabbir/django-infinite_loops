from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def contact_me(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message)
        return HttpResponseRedirect('thank-you')
    return render(request, 'contact_me/contact_me.html')


def thank_you(request):
    return render(request, 'contact_me/thank_you.html')
