from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields=('author', 'title', 'body', 'created_at')
        model=Post

        