from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializers, UserSerializer
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

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=get_user_model().objects.all()
    serializer_class = UserSerializer
        