import json

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *


class AddGallery(APIView):
    def post(self, request):
        request_data = request.data
        data = json.loads(request_data['data'])
        print(data)
        new_gallery = Gallery.objects.create(owner=request.user,
                                             title=data['title'],
                                             subtitle=data['subtitle'],
                                             is_vip=data['is_vip'])
        for f in request.FILES.getlist('image'):
            new_gallery.image = f
            new_gallery.save(update_fields=['image'])

        for f in request.FILES.getlist('images'):
            Image.objects.create(gallery=new_gallery,image=f)

        return Response(status=200)


class UpdateGallery(APIView):
    def post(self, request):
        request_data = request.data
        album = request_data['album']
        action = request_data['action']
        print(album['id'])
        if action == 'delete':
            Gallery.objects.get(id=album['id']).delete()

        return Response(status=200)


class GetGalleriesByUserNickname(generics.ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        galleries = Gallery.objects.filter(owner__nickname=nickname)
        print(galleries)
        return galleries


class AddImageInGalleryById(APIView):
    def post(self,request):
        gallery_id = request.data['gallery_id']
        for f in request.FILES.getlist('image'):
            new_image = Image.objects.create(gallery_id=gallery_id,image=f)
        return Response({'new_id':new_image.id},status=200)



class DeleteImageById(generics.DestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.filter()
