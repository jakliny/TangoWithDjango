from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
>>>>>>> 3300524e77a8f1d8de98f3d6a4977bb851b8d9d4

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
<<<<<<< HEAD
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======

)
>>>>>>> 3300524e77a8f1d8de98f3d6a4977bb851b8d9d4
