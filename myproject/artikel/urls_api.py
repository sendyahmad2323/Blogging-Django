from django.urls import path
from artikel.api import (
    api_artikel_blog_list
)

urlpatterns = [
    ########################## Fungsi Api Artikel ######################
    path('artikel/list',api_artikel_blog_list),
]
