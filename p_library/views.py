from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from p_library.forms import AuthorForm, ReaderForm
from p_library.models import Author, Book, Reader


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorRead(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorUpdate(UpdateView):
    model = Author
    success_url = reverse_lazy('p_library:author_list')
    fields = ["full_name", "birth_year", "country"]
    template_name = 'author_edit.html'


class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    # books_count = books.count()
    biblio_data = {
        "title": "БИБЛИОТЕКУ",
        "books": books
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


AuthorFormSet = formset_factory(AuthorForm, extra=2)


def author_create_many(request):
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='author')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


class ReaderCreate(CreateView):
    model = Reader
    form_class = ReaderForm
    success_url = reverse_lazy('p_library:reader_list')
    template_name = 'reader_edit.html'


class ReaderRead(ListView):
    model = Reader
    template_name = 'reader_list.html'


class ReaderUpdate(UpdateView):
    model = Reader
    success_url = reverse_lazy('p_library:reader_list')
    #fields = []
    form_class = ReaderForm
    template_name = 'reader_edit.html'


class ReaderDelete(DeleteView):
    model = Reader
    form_class = ReaderForm
    #fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:reader_list')
    template_name = 'reader_delete.html'