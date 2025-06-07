from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from artikel.models import ArtikelBlog
from artikel.serializers import ArtikelBlogSerializer

@api_view(['GET'])
def api_artikel_blog_list(request):
    artikel = ArtikelBlog.objects.all()
    serializer = ArtikelBlogSerializer(artikel, many=True)
    content = {
        "message":"berhasil",
        "record":artikel.count(),
        "rows":serializer.data
    }
    return Response(content, status=status.HTTP_200_OK)