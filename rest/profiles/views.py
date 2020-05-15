from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
import os
from rest_framework.generics import *
from plugins.permissions import IsOwner

# Create your views here.
''' @csrf_exempt
@api_view()
def profile_list(request):
    if request.method == 'GET':
        profiles = Profiles.objects.all()
        ser = ProfileSerializer(profiles,many=True)
        return JsonResponse(ser.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request,media_type="text/plain; charset=utf-8")
        ser = ProfileSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            return JsonResponse(ser.errors, status=400)


def file(request):
    fl_path = 'hello.txt'
    filename = 'hello.txt'

    fl = open('profiles/hello.txt', 'r')
    
    response = HttpResponse(fl)
    return response '''


class ProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    
    

class ProfileDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    permission_classes = (IsOwner,)

class FileView(CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

