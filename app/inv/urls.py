from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
                    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, \
                        SubCategoriaDel, MarcaView, MarcaNew, MarcaEdit, marca_inactivar, \
                            UMNew, UMEdit, um_inactivar, UMView, ProductoView, ProductoNew, ProductoEdit, producto_inactivar


urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new/', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(), name='categoria_del'),
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new/', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>',SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/new/', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:pk>',marca_inactivar, name='marca_inactivar'),

    path('um/', UMView.as_view(), name='um_list'),
    path('um/new/', UMNew.as_view(), name='um_new'),
    path('um/edit/<int:pk>',UMEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:pk>',um_inactivar, name='um_inactivar'),



    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new/', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>',ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:pk>',producto_inactivar, name='producto_inactivar'),
]