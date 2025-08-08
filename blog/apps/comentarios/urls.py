from django.urls import path
from . import views 

app_name = "comentarios"


urlpatterns = [
    path('Comentar/<int:pk>', views.Comentar, name='path_comentar'),
    path('EliminarComentario/<int:pk>', views.EliminarComentario.as_view(), name = "path_eliminar_comentario"),
    path('EditarComentario/<int:pk>', views.EditarComentario.as_view(), name = "path_editar_comentario"),

    path('LikeComentario/<int:pk_comentario>/<int:pk_articulo>', views.LikearComentario, name="path_likear_comentario"),
    path('DeslikeComentario/<int:pk_comentario>/<int:pk_articulo>', views.DeslikearComentario, name="path_deslikear_comentario")
]