from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def Toko(request):
    template_name = "landingpage/index.html"
    kategori_list = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    print(artikel)
    
    context = {
        "title": "Toko Jersey",
        "Kategori": kategori_list,  
        "artikel": artikel
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "landingpage/detail_artikel.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found_artikel)
    
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)
    
    context = {
        "title":"Artikel",
        "artikel": artikel,
        "artikel_lainnya":artikel_lainnya
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "artikel_not_found.html"
    return render(request, template_name)


def about(request):
    template_name = "about.html"
    context = {
        "title":"CV Sendy Ahmad"
    }
    return render(request, template_name, context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"Selamat Datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"Selamat Datang"
    }
    return render(request, template_name, context)