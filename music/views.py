from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MusicListView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        music_list = [
            {"name": "最远的你是我最近的爱"},
            {"name": "成都"},
            {"name": "北京欢迎您"}]

        return Response({"data": music_list}, status=status.HTTP_200_OK)
