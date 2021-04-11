import json
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from chat.models import Chat

class GetStreamsByUserNickmane(generics.ListAPIView):
    serializer_class = StreamSerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        streams = Stream.objects.filter(streamer__nickname=nickname, is_archived=False)
        return streams


class GetStreamByUID(generics.RetrieveAPIView):
    serializer_class = StreamSerializer

    def get_object(self):
        uid = self.request.query_params.get('uid')
        try:
            stream = Stream.objects.get(uid=uid, is_active=True)
            return stream
        except:
            return False


class GetStreamsForHomePage(generics.ListAPIView):
    serializer_class = StreamSerializer

    def get_queryset(self):
        streams = Stream.objects.filter(is_archived=False,is_private=False)
        return streams


class AddStream(APIView):
    def post(self, request):
        request_data = request.data
        data = json.loads(request_data['data'])

        new_stream = Stream.objects.create(streamer=request.user,
                                           name=data['name'],
                                           description=data['description'],
                                           is_vip=data['is_vip'],
                                           is_private=data['is_private'],
                                           date=data['date'])
        for f in request.FILES.getlist('image'):
            new_stream.image = f
            new_stream.save(update_fields=['image'])
        new_chat = Chat.objects.create(is_stream_chat=True,stream=new_stream,starter=request.user)
        new_chat.users.add(request.user)
        return Response(status=200)


class UpdateStream(APIView):
    def post(self, request):
        data = request.data
        stream = Stream.objects.get(id=data['id'])
        if data['action'] == 'delete':
            stream.delete()
        elif data['action'] == 'start':
            stream.is_active = True
            stream.save()
        elif data['action'] == 'stop':
            stream.is_active = False
            stream.save()
        return Response(status=200)


class AddRemoveLike(APIView):
    def post(self, request):
        data = request.data
        print(data)
        stream_id = data['stream_id']
        if data['action'] == 'add':
            try:
                stream_likes = StreamLike.objects.get(stream_id=stream_id)
            except:
                stream_likes = StreamLike.objects.create(stream_id=stream_id)
                stream_likes.stream.streamer.streamer_rating+=1
                stream_likes.stream.streamer.save()

            stream_likes.users.add(request.user)
        else:
            stream_likes = StreamLike.objects.get(stream_id=stream_id)
            stream_likes.users.remove(request.user)
        return Response(status=200)