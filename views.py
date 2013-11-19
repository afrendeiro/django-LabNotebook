from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from labnotebook.models import Entry, Notebook
from django.contrib.syndication.views import Feed
from django.contrib.flatpages.models import FlatPage

def getEntries(request, selected_page=1):
    # Get all labnotebook entries
    entries = Entry.objects.all().order_by('-pub_date')

    # Add pagination
    pages = Paginator(entries, 5)

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the entries
    return render_to_response('entries.html', { 'entries':returned_page.object_list, 'page':returned_page})

def getEntry(request, notebookSlug, entrySlug):
	# Get specified entry
	entry = Entry.objects.filter(slug=entrySlug)[0] # gets a dic of entries, so select only one there [0]

	# Display specified entry
	return render_to_response('entry.html', { 'entry':entry })

def getNotebooks(request):
    """Returns list of notebooks"""
    notebooks = Notebook.objects.all()
    return render_to_response('notebooks.html', {'notebooks':notebooks})

def getNotebook(request, notebookSlug):
    """Return entries associated with notebook"""
    entries = Entry.objects.filter(notebook='oikopleura')
    return render_to_response('notebook.html', { 'notebook':notebookSlug, 'entries':entries })

def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    entries = Entry.objects.all().order_by('-pub_date')
    category_entries = []
    for entry in entries:
        if entry.categories.filter(slug=categorySlug):
            category_entries.append(entry)

    # Add pagination
    pages = Paginator(category_entries, 5)

    # Get the category
    category = Category.objects.filter(slug=categorySlug)[0]

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the entries
    return render_to_response('category.html', { 'entries': returned_page.object_list, 'page': returned_page, 'category': category})

class EntriesFeed(Feed):
    title = ""
    link = "feeds/"
    description = ""

    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text