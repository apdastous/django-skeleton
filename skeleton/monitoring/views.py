from django.http import HttpResponse


def ping(request):
    return HttpResponse('OK')
