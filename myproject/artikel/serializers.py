from rest_framework import serializers
from artikel.models import ArtikelBlog

class ArtikelBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtikelBlog
        fields = ['kategori', 'judul', 'konten', 'gambar', 'status', 'created_at', 'created_by']