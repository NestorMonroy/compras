from django.urls import path

from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedorInactivar


urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name='proveedores_list'),
    path('proveedores/new/', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:pk>',proveedorInactivar, name='proveedor_inactivar'),

]