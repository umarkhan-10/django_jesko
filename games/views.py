from django.shortcuts import render
from games.models import Games  # ✅ Make sure this model exists and is migrated

def game(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ handles file uploads
        message = request.POST.get('message')

        if name and image and message:  # optional: basic validation
            games_obj = Games(name=name, image=image, message=message)
            games_obj.save()

    return render(request, 'game.html')
