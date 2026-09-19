from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_published=True).order_by("-published_at")
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
    lookup_field = "slug"