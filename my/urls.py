from django.contrib import admin
from django.urls import path, include
from p_library import views

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', views.books_list),
    path('', include('p_library.urls')),
    path('', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
]

