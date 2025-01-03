from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('project', views.project, name='project'),
    path('quote', views.quote, name='quote'),
    path('service', views.service, name='service'),
    path('training', views.training, name='training'),
]