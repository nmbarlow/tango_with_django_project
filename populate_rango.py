import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
 'tango_with_django_project.settings') # Must do this first

# Must do this way else will get an exception as infrastructure not been initialised yet
import django
django.setup() # Import Django project's settings
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionarie containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title" : "Official Python Tutorial",
         "url" : "http://docs.python.org/2/tutorial/",
         "pviews" : "54"},
        {"title" : "How to Think like a Computer Scientist",
         "url" : "http://www.greenteapress.com/thinkpython/",
         "pviews" : "67"},
        {"title" : "Learn Python in 10 Minutes",
         "url" : "http://www.korokithakis.net/tutorials/python/",
         "pviews" : "23"}
    ]

    django_pages =[
        {"title" : "Official Django Tutorial",
         "url" : "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "pviews" : "115"},
        {"title" : "Django Rocks",
         "url" : "http://www.djangorocks.com/",
         "pviews" : "675"},
        {"title" : "How to Tango with Django",
         "url" : "http://www.tangowithdjango.com/",
         "pviews" : "6789"}
    ]

    other_pages = [
        {"title" : "Bottle",
         "url" : "http://bottlepy.org/docs/dev/",
         "pviews" : "43"},
        {"title" : "Flask",
         "url" : "http://flask.pocoo.org",
         "pviews" : "22"}
    ]

    cats = {"Python" : {"pages" : python_pages, "views" : 128, "likes" : 64},
            "Django" : {"pages" : django_pages, "views" : 64, "likes" : 32},
            "Other Frameworks" : {"pages" : other_pages, "views" : 32, "likes" : 16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"]) # Do category first as page needs category ref.
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["pviews"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print( "- {0} - {1}". format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Execution will start here as the others are 'methods' and therefore will not run
# unless they are called specifically.
# This will only be executed when the module is run as a standalone Python script.
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
