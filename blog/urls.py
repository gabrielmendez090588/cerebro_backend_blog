from django.urls import path
from . import views

#ENDPOINTS ---> puntos de entrada
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('blog', views.lista_posts,name='lista_post'),
    path('post/<int:id>/', views.detalle_post, name='detalle_post'),

]

