from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name="about")
<<<<<<< HEAD
                        )
=======
                       )

>>>>>>> 3300524e77a8f1d8de98f3d6a4977bb851b8d9d4
