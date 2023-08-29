from django.urls import path
from picks.views import Top100ViewSet

urlpatterns = [
    path('', Top100ViewSet.Top100Api)
]
