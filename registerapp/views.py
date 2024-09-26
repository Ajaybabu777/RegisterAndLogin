from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

@csrf_exempt
def register(request):
    try:
        if request.method != "POST":
            raise Exception("method is not allowed",status.HTTP_405_METHOD_NOT_ALLOWED)

        else:
            data = json.loads(request.body)

            esmail = data["email"]
            usallname = data["username"]
            passsswordd = data["password"]

            if not esmail or not usallname or not passsswordd:
                raise Exception ("Data not passed or Incorrupted data passed",status.HTTP_400_BAD_REQUEST)

            else:
                user = User.objects.create(username=usallname,email=esmail,password=passsswordd)

                user.save()

                return JsonResponse ({
                    "message":f"user {usallname} registerd",
                    "status": "Succes"
                })
    

    except Exception as ex:
        return JsonResponse({
            "status":"Failed",
            "message":str(ex)
        })

@csrf_exempt
def login(request):
    try:
        if request.method != "POST":
            raise Exception("method not allowed", status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else:
            data = json.loads(request.body)
            usalname = data["username"]
            passworddddd = data["password"]

            if not usalname or not passworddddd:
                raise Exception("Data not passed or incorrect data passed", status.HTTP_400_BAD_REQUEST)
            
            else:
                user = authenticate(request, username= usalname, password = passworddddd)

                if user is not None:
                    refrest = RefreshToken.for_user(user)

                    return JsonResponse({
                        "refreshToken":str(refrest),
                        "accesstoken":str(refrest.access_token)
                    })


            
    except Exception as ex:
        return JsonResponse({
            "status":"failed",
            "message":str(ex)
        })