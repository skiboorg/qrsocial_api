import json

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *

class GetPostsByUserNickmane(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        nickname = self.request.query_params.get('nickname')
        posts = Post.objects.filter(owner__nickname=nickname).order_by('-created_at')
        return posts


class DeletePost(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        Post.objects.get(id=data['id']).delete()
        return Response(status=200)


class AddPost(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        new_post = Post.objects.create(owner=request.user, text=json.loads(request.data['text']))
        for f in request.FILES.getlist('image'):
            # print(f)
            new_post.image = f
            new_post.save(update_fields=['image'])

        return Response(status=200)


class AddComment(APIView):
    def post(self, request):
        data = request.data
        PostComment.objects.create(owner=request.user,
                                   post_id=data['post_id'],
                                   text=data['text'])
        return Response(status=200)


class AddRemoveLikeToPost(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'add':
            try:
                post_likes = PostLike.objects.get(post_id=data['post_id'])
            except:
                post_likes = PostLike.objects.create(post_id=data['post_id'])

            post_likes.users.add(request.user)
        else:
            post_likes = PostLike.objects.get(post_id=data['post_id'])
            post_likes.users.remove(request.user)
        return Response(status=200)


