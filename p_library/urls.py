from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from .views import AuthorCreate, AuthorRead, author_create_many, AuthorUpdate, AuthorDelete
from .views import ReaderCreate, ReaderRead, ReaderUpdate, ReaderDelete
from .views import BookCreate, BookRead, BookUpdate, BookDelete

app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorRead.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(),
         name='author_delete'),
    path('author/create_many/', author_create_many,
         name='author_create_many'),

    path('reader/create/', ReaderCreate.as_view(), name='reader_create'),
    path('reader/', ReaderRead.as_view(), name='reader_list'),
    path('reader/<int:pk>/', ReaderUpdate.as_view(), name='reader_edit'),
    path('reader/<int:pk>/delete/', ReaderDelete.as_view(),
         name='reader_delete'),

    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('book/', BookRead.as_view(), name='book_list'),
    path('book/<int:pk>/', BookUpdate.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDelete.as_view(),
         name='book_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)