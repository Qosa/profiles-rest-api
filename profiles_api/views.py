from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview = [
            'blah blah blah ksssszzzzzzz!'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})