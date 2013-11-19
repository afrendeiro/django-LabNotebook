from django.conf.urls import patterns, include, url
from labnotebook import views

urlpatterns = patterns('',
	# Front page
	url(r'^$', views.getNotebooks, name='notebooks'),
    #url(r'^$', views.getEntries, name='entries'),
    # Front page paginated
    #url(r'^(?P<selected_page>\d+)/?$', views.getEntries, name='entries_pag'),

    # Notebook
    url(r'^(?P<notebookSlug>[-a-zA-Z0-9]+)/?$', views.getNotebook, name='notebook'),

    # Single entry
    url(r'^(?P<notebookSlug>[-a-zA-Z0-9]+)/\d{4}/\d{1,2}/(?P<entrySlug>[-a-zA-Z0-9]+)/?$', views.getEntry, name ='entry'),
   
    # Categories
    url(r'^categories/(?P<categorySlug>\w+)/?$', views.getCategory, name='category'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', views.getCategory, name='category_pag'),

    
)