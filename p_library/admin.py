from django.contrib import admin
from .models import (Book, Author, Reader, BookReading)

[admin.site.register(item) for item in (Author, Reader, BookReading,)]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    exclude = []
    fields = []