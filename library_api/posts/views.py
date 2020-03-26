from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializers, UserSerializer
from .permissions import IsAuthourReadOnly
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes= (IsAuthourReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class = UserSerializer
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
        