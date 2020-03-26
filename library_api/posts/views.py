from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated),
    queryset= Post.objects.all()
    serializer_class = PostSerializers

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated),
    queryset = Post.objects.all()
    serializer_class =PostSerializers