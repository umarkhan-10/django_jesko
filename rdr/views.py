from django.shortcuts import render , HttpResponse
from rdr.models import rdr

def rdr(request):
 if request.method == 'POST':
        name = request.POST['name']
        image= request.POST['image']
        message = request.POST['message']
        rdr = rdr(name=name, image=image, message=message,)
        rdr.save()
 return render(request, 'rdr2.html',)