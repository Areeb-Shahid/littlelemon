from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('display_date/', views.display_date, name='display_date'),
    path('booking/', views.form_view),
    path('menu_item/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
]