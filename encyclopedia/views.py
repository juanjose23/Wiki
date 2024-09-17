from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse
from . import util
from markdown2 import Markdown
import random

markdowner = Markdown()



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entry(request, title):
    content = util.get_entry(title)

    if content == None:
        raise Http404()

    is_wiki_page = request.path.startswith('/wiki/')
    html_content = markdowner.convert(content)
    return render(
        request,
        "encyclopedia/entries.html",
        {
            "title": title,
            "content": html_content,
            "is_wiki_page": is_wiki_page,
        },
    )

def search(request):
    searchedTitle = request.GET.get("q")

    # Verificar si searchedTitle es None
    if not searchedTitle:
        # Si no se proporciona un término de búsqueda, mostrar todos los resultados o manejar el error
        return render(   request, "encyclopedia/404.html")
    content = util.get_entry(searchedTitle)

    if content is not None:
        return redirect(reverse('show_entry', args=[searchedTitle]))

    # Si la entrada no existe, buscar entradas que contengan el término de búsqueda
    entries = util.list_entries()

    # Filtrar resultados
    search_results = []
    for entry in entries:
        result = entry.lower().find(searchedTitle.lower())
        if result != -1:
            search_results.append(entry)

    return render(
        request,
        "encyclopedia/index.html",
        {"entries": search_results, "search_param": searchedTitle},
    )


def new_page(request):
    if request.method == "POST":
        title = request.POST.get("page_title")
        content = request.POST.get("page_content")

      


        if util.get_entry(title) != None:
              return render(   request, "encyclopedia/404.html",)
       
        util.save_entry(title, content)
        
        return redirect(reverse('show_entry', args=[title]))

    # If it is a GET request
    return render(request, "encyclopedia/new_page.html")


# currently building
def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("page_content")

        util.save_entry(title, content)

        return redirect(reverse('show_entry', args=[title]))

    # If it is a GET request
    return render(
        request, "encyclopedia/edit_page.html",
        {
            "title": title,
            "content": util.get_entry(title),
        }
    )


def random_page(request):
    pages = util.list_entries()
    random_page = random.choice(pages)
    return redirect(reverse('show_entry', args=[random_page]))