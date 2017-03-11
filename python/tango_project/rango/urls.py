from django.conf.urls import url,patterns
from rango import views

urlpatterns = patterns('',
        url(r'^$' , views.index , name='index'),
        url(r'^about/', views.about , name='about')
        )
