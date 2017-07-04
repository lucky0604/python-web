from django.db.models import Q
from rest_framework.generics import (
  CreateAPIView,
  DestroyAPIView,
  ListAPIView,
  UpdateAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView
)
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated,
)
from backend.models import Post
from .serializers import (
  PostCreateUpdateSerializer,
  PostDetailSerializer,
  PostListSerializer
)

from backend.permissions import IsOwnerOrReadOnly

'''
Articles -------------------------------------
'''
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny,]

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.filter(user = self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__icontains=query)
            ).distinct()

        return queryset_list
