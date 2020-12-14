import json
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *

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
        print(uid)
        try:
            stream = Stream.objects.get(uid=uid)
            return stream
        except Stream.DoesNotExist:
            return False



class GetStreamsForHomePage(generics.ListAPIView):
    serializer_class = StreamSerializer

    def get_queryset(self):
        streams = Stream.objects.filter(is_archived=False,is_private=False)
        return streams

class AddStream(APIView):
    def post(self, request):
        request_data = request.data
        print(json.loads(request_data['data']))
        data = json.loads(request_data['data'])

        new_stream = Stream.objects.create(streamer=request.user,
                                           name=data['name'],
                                           description=data['description'],
                                           is_vip=data['is_vip'],
                                           is_private=data['is_private'],
                                           date=data['date'])
        for f in request.FILES.getlist('image'):
            print(f)
            new_stream.image = f
            new_stream.save(update_fields=['image'])
        return Response(status=200)

class DeleteStream(generics.DestroyAPIView):
    serializer_class = StreamSerializer
    queryset = Stream.objects.filter()
