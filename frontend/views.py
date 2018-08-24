from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from fabric import task, runners
from rest_framework import status
from rest_framework.decorators import api_view


from frontend.models import Settings

from web.celery import app
from frontend.tasks import run_web_server, stop_web_server


def main_index(request):
    return render(request,'index.html')

@api_view
def recode_video(request):
    return render(request,'video.html')


@app.task
def add(x, y):
    return x + y


@api_view(['GET','POST'])
def web_server(request):
    status = request.GET.get('data')

    text = ''
    query = Settings.objects.get(id=1)
    if status == 'open':
        run_web_server(query.ip_address, query.port)
        text = u'웹저장소가 실행되었습니다. \n{0}:{1}로 접속해주세요!' .format(query.ip_address ,query.port)

    else:
        stop_web_server(query.ip_address, query.port)
        text = u'웹저장소가 종료되었습니다.'


    return JsonResponse({'message': text, 'status' : status})

@api_view
def feed_back(request):
    return

@api_view
def settings(request):
    return