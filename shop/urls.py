from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),
    path('create-offer/', views.create_offer, name='create_offer'),
    path('update-offer/<int:pk>/', views.update_offer, name='update_offer'),
    path('delete-offer/<int:pk>/', views.delete_offer, name='delete_offer'),
]
