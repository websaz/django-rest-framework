from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError
import re
from posts.serializers import PostSerializer
from posts.models import Posts
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ProfileSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    post = PostSerializer(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    user = serializers.CharField(read_only=True)
    
    
    class Meta:
        model = Profiles
        fields = '__all__'

    def validate_phone_number(self,value):
        phone_number_pattern = re.compile("^09\d{9}$")
        if phone_number_pattern.match(value):
            return value
        else:
            raise ValidationError("phone number is not correct.")

    def create(self,validated_data):
        if 'post' in validated_data:
            users = validated_data.pop('user_id')
            profile_user = get_object_or_404(User,pk=users)
            post = validated_data.pop('post')
            profile = Profiles.objects.create(user=profile_user,**validated_data)
            my_post = Posts.objects.create(**post,author=profile)
            return profile
        else:
            users = validated_data.pop('user_id')
            profile_user = get_object_or_404(User,pk=users)
            profile = Profiles.objects.create(user=profile_user,**validated_data)
            
            return profile
        
        
class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields = '__all__'