from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import Top100Serializer
from .models import Top100
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
from .top100 import ShowTop100

class Top100ViewSet(viewsets.ModelViewSet):
    queryset = Top100.objects.all()
    serializer_class = Top100Serializer

    @api_view(['GET'])
    def Top100Api(request) :
        try :
            resultList = ShowTop100.show()
            print(type(resultList))
            # serializer = Top100Serializer(resultList, many=True)
            # print("serializer: " + serializer.data)
            return Response(json.dumps(resultList, ensure_ascii=False))
        except Exception as e :
            print('dead')
            print(e)
            response = {'message': 'Invalid request method'}
            return JsonResponse(response, status=400)
        

# class GenreViewSet(viewsets.ModelViewSet):
#     queryset = Top100.objects.all()
#     serializer_class = Top100Serializer

#     @api_view(['GET'])
#     def GenreApi(request, selected):
#         try:
#             selectList = []
#             selectList.append(SelectedGenres.selected(list(selected.split(','))))
#             serializer = SelectedGenres(selectList)
#             print(serializer.data)
#             return JsonResponse(serializer.data)
#         except:
#             response = {'message': 'Invalid request method'}

#             return JsonResponse(response, status=400)