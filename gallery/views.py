import json

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *


class GetLastUserImages(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.query_params.get('id')).order_by('-created_at')[:4]


class GetLastGallery(generics.ListAPIView):
    serializer_class = GalleryFullSerializer

    def get_queryset(self):
        return Gallery.objects.filter(owner__is_streamer=True)[:5]


class GetVideos(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        items = None
        if self.request.query_params.get('type') == 'index':
            items = Video.objects.all()[:10]
        if self.request.query_params.get('type') == 'all':
            items = Video.objects.all()
        if self.request.query_params.get('nick'):
           items = Video.objects.filter(owner__nickname=self.request.query_params.get('nick'))
        return items


class AddVideo(APIView):
    def post(self, request):
        request_data = request.data
        data = json.loads(request_data['data'])
        print(request.FILES)
        new_video = Video.objects.create(owner=request.user,
                                        title=data['title'],
                                        is_vip=data['is_vip'])
        for f in request.FILES.getlist('image'):
            new_video.image = f
            new_video.save(update_fields=['image'])
        for f in request.FILES.getlist('file'):
            new_video.file = f
            new_video.save(update_fields=['file'])

        return Response(status=200)
class AddGallery(APIView):
    def post(self, request):
        request_data = request.data

        data = json.loads(request_data['data'])
        new_gallery = Gallery.objects.create(owner=request.user,
                                             title=data['title'],
                                             subtitle=data['subtitle'],
                                             is_vip=data['is_vip'])
        for f in request.FILES.getlist('image'):
            new_gallery.image = f
            new_gallery.save(update_fields=['image'])

        for f in request.FILES.getlist('images'):
            Image.objects.create(owner=request.user, gallery=new_gallery,image=f)
        return Response(status=200)


class UpdateGallery(APIView):
    def post(self, request):
        request_data = request.data
        album = request_data['album']
        action = request_data['action']
        if action == 'delete':
            Gallery.objects.get(id=album['id']).delete()
        return Response(status=200)


class GetBanners(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class GetVideosByUserNickname(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        return Video.objects.filter(owner__nickname=nickname)


class GetGalleriesByUserNickname(generics.ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        galleries = Gallery.objects.filter(owner__nickname=nickname)
        return galleries


class AddImageInGalleryById(APIView):
    def post(self,request):
        print(request.data)
        gallery_id = request.data['gallery_id']
        new_image = None
        for f in request.FILES.getlist('image'):
            new_image = Image.objects.create(owner=request.user, gallery_id=gallery_id, image=f)
        return Response({'new_id':new_image.id}, status=200)


class DeleteImageById(generics.DestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.filter()
