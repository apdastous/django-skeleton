import datetime
from random import choice

from django.http import HttpResponse
from django.shortcuts import render


def root(request):
    messages = [
        'Yes.',
        'No.',
        'Maybe.',
        'Ask again later.',
        'Outlook not so good.',
        'Most definitely.',
        'Seek help.',
        'Absolutely.',
        'Without a doubt.',
        'Never.',
        'As God as my witness, this shall be.',
        'Why would you even ask that?',
        'Girl, please.',
        'Indubitably.'
    ]

    fortune = choice(messages)

    return render(request, 'root.html', {'fortune': fortune, 'datetime': datetime.datetime.now()})
