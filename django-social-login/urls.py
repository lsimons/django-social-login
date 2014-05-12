from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', TemplateView.as_view(template_name="home.html")),
    url('^login/?$', TemplateView.as_view(template_name="login.html")),
    url('^login/failure/?$', TemplateView.as_view(template_name="login_failure.html")),
    url('^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
