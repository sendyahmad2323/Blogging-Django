from django.urls import path
from artikel.views import (
    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,
    admin_artikel_list,
    admin_artikel_tambah,
    admin_artikel_update,
    admin_artikel_delete,
)

urlpatterns = [
    path('kategori/list', admin_kategori_list, name="admin_kategori_list"),
    path('kategori/tambah', admin_kategori_tambah, name="admin_kategori_tambah"),
    path('kategori/update/<int:id_kategori>', admin_kategori_update, name="admin_kategori_update"),
    path('kategori/delete/<int:id_kategori>', admin_kategori_delete, name="admin_kategori_delete"),
    
    path('artikel/list', admin_artikel_list, name="admin_artikel_list"),
    path('artikel/tambah', admin_artikel_tambah, name="admin_artikel_tambah"),
    path('artikel/update/<int:id_artikel>', admin_artikel_update, name="admin_artikel_update"),
    path('artikel/delete/<int:id_artikel>', admin_artikel_delete, name="admin_artikel_delete"),
]
