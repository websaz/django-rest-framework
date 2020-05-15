from django.shortcuts import render
from .models import *
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def posts_list(request):
    if request.method == 'GET':
        posts = Posts.objects.all()
        ser = PostSerializer(posts,many=True)
        return JsonResponse(ser.data, safe=False)