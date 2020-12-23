from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *


class AddGallery(APIView):
    def post(self,request):
        print(request.data)
        return Response(status=200)


class DeleteGallery(APIView):
    def post(self, request):
        return Response(status=200)


class GetGalleriesByUserNickname(generics.ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        galleries = Gallery.objects.filter(owner__nickname=nickname)
        print(galleries)
        return galleries


