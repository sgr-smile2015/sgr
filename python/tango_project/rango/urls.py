from django.conf.urls import url,patterns
from rango.views import * 

urlpatterns = patterns('',
        url(r'^$' , index , name='index'),
        url(r'^about/', about , name='about')
        )

#from rango import views

#urlpatterns = patterns('',
#        url(r'^$' , views.index , name='index'),
#        url(r'^about/', views.about , name='about')
#        )
