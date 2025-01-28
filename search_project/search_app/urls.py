from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.search_view), 
    path('search/', views.search_view, name='search_view'), 
    path('product/new/', views.product_create, name='product_create'), 
    path('product/<int:pk>/', views.product_detail, name='product_detail'), 
    path('product/<int:pk>/edit/',  views.product_update, name='product_update'), 
    path('product/<int:pk>/delete',  views.product_delete, name='product_delete'), 
    path('products/', views.product_list, name='product_list'),
    path('products/category/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/performance', views.performance_view ,name='performance'),
    path('about-site/', views.about_site_view, name='about_site'),

]

