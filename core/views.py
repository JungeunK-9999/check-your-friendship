from django.shortcuts import render, redirect, get_object_or_404
from core.models import Player
from static.questions import questions


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


def create_user(request):
    player = Player.objects.create(name=request.POST['name'])
    if request.POST['is_host'] == 'True':
        player.is_host = True
        player.host_number = player.id
    else:
        player.host_number = int(request.POST['host_number'])
    player.save()
    return redirect(f'quiz/{player.id}')


def quiz(request, pk):
    player = get_object_or_404(Player, id=pk)
    current_question = player.current_question
    question = questions[current_question - 1]
    ctx = {
        'player': player,
        'current_question': current_question,
        'false': question['false'],
        'true': question['true'],
    }
    player.save()
    return render(request, 'quiz.html', ctx)


def check(request, pk):
    player = get_object_or_404(Player, id=pk)
    choice = request.POST['choice']

    if choice == "True":
        choice = True
    else:
        choice = False

    if player.current_question == 1:
        player.question1 = choice
    elif player.current_question == 2:
        player.question2 = choice
    elif player.current_question == 3:
        player.question3 = choice
    elif player.current_question == 4:
        player.question4 = choice
    elif player.current_question == 5:
        player.question5 = choice
    elif player.current_question == 6:
        player.question6 = choice
    elif player.current_question == 7:
        player.question7 = choice
    elif player.current_question == 8:
        player.question8 = choice
    elif player.current_question == 9:
        player.question9 = choice
    elif player.current_question == 10:
        player.question10 = choice
    else:
        return render(request, 'error.html')

    player.current_question += 1
    player.save()

    if player.current_question > 10:
        return render(request, 'result.html', {'player': player})

    return quiz(request, pk)
