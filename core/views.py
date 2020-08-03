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
                           'host_number': host_number}
                          )
    return render(request, 'main.html')


def create_user(request):
    player = Player.objects.create(name=request.POST['name'])
    if request.POST['is_host'] == 'True':
        player.is_host = True
        player.host_number = -1
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
        return redirect('result', player.id)

    return quiz(request, pk)


def result(request, pk):
    player = get_object_or_404(Player, id=pk)
    if player.is_host == False:
        host = get_object_or_404(Player, id=player.host_number)

        if host.question1 == player.question1:
            player.score += 1
        if host.question2 == player.question2:
            player.score += 1
        if host.question3 == player.question3:
            player.score += 1
        if host.question4 == player.question4:
            player.score += 1
        if host.question5 == player.question5:
            player.score += 1
        if host.question6 == player.question6:
            player.score += 1
        if host.question7 == player.question7:
            player.score += 1
        if host.question8 == player.question8:
            player.score += 1
        if host.question9 == player.question9:
            player.score += 1
        if host.question10 == player.question10:
            player.score += 1
        player.save()

    if player.is_host:
        guests = {}
    else:
        guests = Player.objects.filter(host_number=player.host_number).order_by('-score')

    ctx = {
        'player': player,
        'is_guest': not (player.is_host),
        'guests': guests
    }

    return render(request, 'result.html', ctx)
