from django.urls import path, include
from .views import MbtiPredictApi

urlpatterns = [
    path('<str:gernecnt>/', MbtiPredictApi),
]

