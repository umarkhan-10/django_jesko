from django.shortcuts import render , HttpResponse
from contact.models import Contact

def contact(request):
 if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact=Contact(name=name, email=email, message=message)
        contact.save()
 return render(request, 'contact.html',)
