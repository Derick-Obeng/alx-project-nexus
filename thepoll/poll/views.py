from django.http import HttpResponse
from django.shortcuts import redirect,render, get_object_or_404
from django.db.models import F
from .models import Poll , Choice
from django.urls import reverse



def poll_list(request):
    polls = Poll.objects.order_by('-pub_date')
    return render(request, 'poll/index.html', {'polls': polls})
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    return render(request, 'poll/index.html', {'latest_poll_list': latest_poll_list})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choices = Choice.objects.filter(poll=poll)
    return render(request, 'poll/detail.html', {'poll': poll, 'choices': choices})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choice_id = request.POST.get('choice')

    if not choice_id:
        return render(request, 'poll/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })

    selected_choice = get_object_or_404(Choice, pk=choice_id, poll=poll)
    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    return redirect('poll_results', poll_id=poll.id)
    
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choices = poll.choice_set.all()
    total_votes = sum(c.votes for c in choices)

    for c in choices:
        if total_votes > 0:
            c.percent = (c.votes / total_votes) * 100
        else:
            c.percent = 0

    return render(request, 'poll/results.html', {
        'poll': poll,
        'choices': choices,
        'total_votes': total_votes
    })
