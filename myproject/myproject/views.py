from django.shortcuts import render, redirect
from django.db.models import Count
from artikel.models import Kategori, ArtikelBlog
from django.contrib.auth import login, get_user_model
from google.oauth2 import id_token
from google.auth.transport import requests

def Toko(request):
    template_name = "landingpage/index.html"
    kategori_list = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    print(artikel)
    
    context = {
        "title": "Selamat Datang",
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
    
    # Jumlah total kategori
    jumlah_kategori = Kategori.objects.count()

    # Artikel terbaru
    artikel_terbaru = ArtikelBlog.objects.all().order_by('-created_at')[:5]

    # Total artikel
    total_artikel = ArtikelBlog.objects.count()

    # Kategori populer
    kategori_populer_qs = (
        ArtikelBlog.objects.values('kategori__nama')
        .annotate(jumlah=Count('kategori'))
        .order_by('-jumlah')
        .first()
    )
    kategori_populer = kategori_populer_qs['kategori__nama'] if kategori_populer_qs else 'Belum ada'

    # Daftar kategori dan jumlah artikel masing-masing
    categories = Kategori.objects.all()
    category_labels = [k.nama for k in categories]
    category_counts = [k.artikelblog_set.count() for k in categories]

    return render(request, 'dashboard/index.html', {
        'jumlah_kategori': jumlah_kategori,
        'artikel_terbaru': artikel_terbaru,
        'total_artikel': total_artikel,
        'kategori_populer': kategori_populer,
        'user': request.user,
        'category_labels': category_labels,
        'category_counts': category_counts,
    })
def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"Selamat Datang"
    }
    return render(request, template_name, context)


def user_dashboard(request):
    artikel_terbaru = ArtikelBlog.objects.all().order_by('-created_at')[:5]
    total_artikel = ArtikelBlog.objects.count()
    kategori_populer = (
        ArtikelBlog.objects.values('kategori')
        .annotate(jumlah=Count('kategori'))
        .order_by('-jumlah')
        .first()
    )
    return render(request, 'dashboard/pengguna/dashboard_user.html', {
        'artikel_terbaru': artikel_terbaru,
        'total_artikel': total_artikel,
        'kategori_populer': kategori_populer['kategori'] if kategori_populer else 'Belum ada',
        'user': request.user,
    })

def gallery_view(request):
    artikel = ArtikelBlog.objects.all()
    return render(request, 'landingpage/gallery.html', {'artikel': artikel})

def dashboard_gallery(request):
    artikel_list = ArtikelBlog.objects.all().order_by('-created_at')
    return render(request, 'dashboard/gallery.html', {'artikel_list': artikel_list})

def google_gis_callback(request):
    token = request.POST.get('credential')
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            "77864412996-lmvfgb4g0g99nl6kpogsfn7r1kukmbqq.apps.googleusercontent.com"
        )
        email = idinfo.get('email')
        User = get_user_model()
        user, created = User.objects.get_or_create(email=email, defaults={'username': email})
        login(request, user)
        return redirect('dashboard')  # Sekarang berhasil setelah POST
    except Exception as e:
        print(f"Error login GIS: {e}")
        return redirect('auth-login')