from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from fabric import task, runners
from rest_framework import status
from rest_framework.decorators import api_view


from frontend.models import Settings
from frontend.serializers import SettingsSerializer

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

@api_view(['GET'])
def env_settings(request):
    query = Settings.objects.get(id=1)
    settings_serializers = SettingsSerializer(query).data
    ip_array = settings_serializers['ip_address'].split('.')
    settings_serializers['ip1'] = ip_array[0]
    settings_serializers['ip2'] = ip_array[1]
    settings_serializers['ip3'] = ip_array[2]
    settings_serializers['ip4'] = ip_array[3]
    return render(request, 'env.html', settings_serializers)

@api_view(['GET'])
def change_env_values(request):
    value = request.GET.get('value')
    get_type = request.GET.get('type')
    if get_type == 'fps':
        env = Settings.objects.get(id=1)
        env.fps = value
        env.save()
    if get_type == 'port':
        env = Settings.objects.get(id=1)
        env.port = value
        env.save()
    if get_type == 'ip_address':
        env = Settings.objects.get(id=1)
        env.ip_address = value
        env.save()
    if get_type == 'batch_size':
        env = Settings.objects.get(id=1)
        env.batch_size = value
        env.save()
    text = '정상적으로 변경되었습니다.'
    return JsonResponse({'message': text})
