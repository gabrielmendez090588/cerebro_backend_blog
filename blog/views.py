from django.shortcuts import render
from .models import Post

# Create your views here.
def inicio(request):
    publicaciones = [
        "Post 1: Django es increíble",
        "Post 2: Qué es MVT (Modelo-Vista-Template)",
        "Post 3: Cómo crear una app en Django",

    ]
    return render(request, 'blog/inicio.html', {'posts': publicaciones})

def sobre_mi(request):
    return render(request, 'blog\sobre_mi.html') # type: ignore

 

def lista_posts(request):
    posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})
