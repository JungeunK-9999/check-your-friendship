from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from core.models import Player
from static.questions import questions


# Create your views here.
def starting(request):
    if request.method == 'POST':
        ctx = {
            'is_host': True,
            'host_number': False
        }
        if request.POST['is_host'] == 'False':
            ctx['is_host'] = False
            ctx['host_number'] = request.POST['host_number']
        return render(request, 'greeting.html', ctx)
    return render(request, 'main.html')


def invitation(request, pk):
    ctx = {}
    ctx['is_host'] = False
    ctx['host_number'] = pk
    return render(request, 'greeting.html', ctx)


def create_user(request):
    player = Player.objects.create(name=request.POST['name'])
    if request.POST['is_host'] == 'True':
        player.is_host = True
        player.host_number = player.id
    else:
        player.host_number = int(request.POST['host_number'])
    player.save()
    return redirect(reverse('quiz', args=[player.id]))


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

    if player.current_question > 10 and player.is_host:
        return redirect('result', player.id)
    elif player.current_question > 10:
        return redirect(reverse('score', args=[pk]))
    return redirect(reverse('quiz', args=[pk]))


def score(request, pk):
    player = get_object_or_404(Player, id=pk)
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

    return redirect(reverse('result', args=[pk]))


def result(request, pk):
    player = get_object_or_404(Player, id=pk)

    guests = Player.objects.filter(host_number=player.host_number, current_question=11, is_host=False).order_by(
        '-score')

    ctx = {
        'player': player,
        'is_guest': not (player.is_host),
        'guests': guests
    }

    return render(request, 'result.html', ctx)
