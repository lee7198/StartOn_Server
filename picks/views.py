from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import Top100Serializer
from .models import Top100
from django.http import JsonResponse

class Top100ViewSet(viewsets.ModelViewSet):
    queryset = Top100.objects.all()
    serializer_class = Top100Serializer

    def top100(request, pk):    
        object = Top100.objects.get(pk=pk)
        if request.method == "GET":
            serializer = Top100Serializer(object)
            return JsonResponse(serializer.data,safe =False)
        
        elif request.method == "PUT":
            serializer = Top100Serializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, ststus=400)
        
        elif request.method == "DELETE":
            serializer = Top100Serializer(object)
            serializer.delete()
            return JsonResponse(serializer.data, status=204)