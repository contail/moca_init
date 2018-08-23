from django.shortcuts import render


# Create your views here.
from fabric import task, runners
from rest_framework.decorators import api_view


def main_index(request):
    return render(request,'index.html')

@api_view
def recode_video(request):
    return render(request,'video.html')


@task
def start_web_server(request):
    #시작 버튼
    #중지 버튼에 따라
    #async 해주기?

    #method == post 이면 시작
    #methos == delete 이면 중지

    # redis + celery 사용해야할지도..
    return

@api_view
def feed_back(request):
    return

@api_view
def settings(request):
    return