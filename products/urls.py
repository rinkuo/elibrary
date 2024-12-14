from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('edit/<int:id>/', views.product_edit, name='product_edit'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('category/create/', views.category_create, name='category_create'),
]