from rest_framework.serializers import (
    HyperlinkedIdentityField,
    SerializerMethodField,
    ModelSerializer
)
from backend.models import Post
from backend.serializers import UserDetailsSerializer
from rest_framework import serializers

'''
Articles ------------------------------------------
'''

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
            'status',
        ]

post_detail_url = HyperlinkedIdentityField(view_name = 'posts-api:detail', lookup_field = 'slug')

class PostListSerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = UserDetailsSerializer(read_only = True)
    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'user',
            'title',
            'content',
            'publish',
            'status',
            'timestamp',
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = UserDetailsSerializer(read_only = True)
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
        ]

    def get_html(self, obj):
        return obj.get_markdown()
