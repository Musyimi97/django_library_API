from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthourReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthourReadOnly),
    queryset= Post.objects.all()
    serializer_class = PostSerializers

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthourReadOnly),
    queryset = Post.objects.all()
    serializer_class =PostSerializers