from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario
from .forms import ComentarioForm
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

   

def detalle_post(request, id):
    post = get_object_or_404(Post, id=id, publicado=True)
    comentarios = post.comentarios.all().order_by('-fecha')  # type: ignore

    
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
    else:
        form = ComentarioForm()

    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })
