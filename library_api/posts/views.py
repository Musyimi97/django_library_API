from rest_framework import permissions
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

        