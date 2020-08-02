from django.shortcuts import render
from core.models import Player


# Create your views here.
def starting(request):
    if request.method == 'POST':
        if request.POST['is_host'] == 'True':
            return render(request, 'greeting.html', {'is_host': request.POST['is_host']})
        else:
            host_number = request.POST['host_number']
            return render(request, 'greeting.html',
                          {'is_host': request.POST['is_host'],
                           'host_number': host_number
                           }
                          )
    return render(request, 'main.html')


def quiz(request):
    player = Player.objects.create(name=request.POST['name'])
    if request.POST['is_host'] == 'True':
        player.is_host = True
        player.host_number = player.id
    else:
        player.host_number = int(request.POST['host_number'])
    player.save()
    return render(request, 'quiz.html')
