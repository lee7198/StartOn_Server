from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mbti
from .serializers import MbtiSerializer
from django.http import JsonResponse
from .Predict import Mbti_predict
from .mbti_game import GameResult

# Create your views here.
@api_view(['GET'])
def MbtiPredictApi(request, gernecnt) :
    try :
        total = Mbti.objects.all()
        print("requeset=",request)
        gerneList = []
        gerneList.append(list(map(int, gernecnt.split(','))))
        # print(gerneList)
        total.mbti, total.Percent = Mbti_predict(gerneList)
        print("mbti 판별 결과\n: ",total.mbti)
        print("mbit 확률 {:.2f}%\n:" .format(total.Percent))
        result = GameResult(total.mbti)
        print(result)
        # serializer = MbtiSerializer(total)
        # print(serializer.data)
        
        # print(type(serializer.data))
        return Response(result)
    except Exception as e :
        print(e)
        response = {'message': 'Invalid request method'}

        return JsonResponse(response, status=400)