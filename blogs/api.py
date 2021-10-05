# views

from .models import BlogDetail
from .serializers import BlogDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def stories_api(request):
    all_blogs = BlogDetail.objects.all()
    data = BlogDetailSerializer(all_blogs, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def story_detail_api(request, id):
    story_detail_detail = BlogDetail.objects.get(id=id)
    data = BlogDetailSerializer(career_detail).data
    return Response({'data': data})


class StoryDetailListApi(generics.ListAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailSerializer


class StoryDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = BlogDetail.objects.all()
    lookup_field = 'id'
