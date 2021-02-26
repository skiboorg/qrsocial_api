from rest_framework import generics
from .serializers import *
from .models import *


class GetItems(generics.ListAPIView):
    serializer_class = BlogItemSerializer

    def get_queryset(self):
        if self.request.query_params.get('is_at_index'):
            blog_items = BlogItem.objects.filter(is_at_home=True)
        else:
            blog_items = BlogItem.objects.all()
        return blog_items


class GetItem(generics.RetrieveAPIView):
    serializer_class = BlogItemSerializer

    def get_object(self):
        blog_item = BlogItem.objects.get(name_slug=self.request.query_params.get('name_slug'))
        return blog_item
