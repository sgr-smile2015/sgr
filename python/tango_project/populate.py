import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_project.settings')

import django
django.setup()
 
from rango.models import Category, Page

def populate():
    python_cat = add_cat('python',128,64)

    add_page( cat=python_cat,
            title="Official Python Tutorial",
            url="http://docs.python.org/2/tutorial/"
            )

    add_page( cat=python_cat,
            title="How to Think like a computer Scientist",
            url="http://www.greenteapress.com/thinkpython/"
            )
    
    add_page( cat=python_cat,
            title="Learn Python in 10 Minutes",
            url="http://www.korokithakis.net/tutorials/python/"
            )
    django_cat = add_cat("django",64,32)

    add_page( cat=django_cat,
            title="Official Django Tutorial",
            url="http://docs.djangoproject.com/en/1.5/intro/tutorial01/"
            )

    add_page( cat=django_cat,
            title="How to Tango with Django",
            url="http://www.tangowithdjango.com/"
            )

    frome_cat = add_cat("other Frameworks",32,18)

    add_page( cat=frome_cat,
            title="Bottle",
            url="http://bottlepy.org/docs/dev/"
            )

    add_page( cat=frome_cat,
            title="Flask",
            url="http://flsk.pocoo.org"
            )

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c),str(p))
    

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat,title=title,url=url,views=views)[0]
    return p

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

if __name__ == '__main__':
    print "insert data to databses"
    populate()
