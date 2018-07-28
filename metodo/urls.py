"""ishikawa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django.views.generic import TemplateView

from .views import crear_hallazgo
from .views import crear_causas
from .views import ListaHallazgos
from .views import amef
from .views import kaizen
from .views import formulario
from .views import editar_causas

app_name = 'metodo'

urlpatterns = [
    url(r'^hallazgo/$', crear_hallazgo, name='hallazgo'),
    url(r'^portada/$', TemplateView.as_view(template_name='metodo/portada.html'), name='portada'),
    url(r'^hallazgo/(?P<pk>\d+)/$', crear_causas, name='causas'),
    url(r'^hallazgo/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', editar_causas, name='editar_causa'),
    url(r'^hallazgo/amef/(?P<pk>\d+)/$', amef, name='amef'),
    url(r'^hallazgo/kaizen/(?P<pk>\d+)/$', kaizen, name='kaizen'),
    url(r'^lista/', ListaHallazgos.as_view(), name='lista_hallazgos'),
    url(r'^formulario/(?P<pk>\d+)/$', formulario, name='formulario'),
]
