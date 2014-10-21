from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import redis


def home(request):
    return render(request, 'index.html', locals())


@csrf_exempt
def send_message(request):
    if request.method == 'POST':

        print request.GET
        message = request.GET['message']
        r = redis.StrictRedis()
        r.publish('my_channel', message)
        print message

        return HttpResponse('OK')
