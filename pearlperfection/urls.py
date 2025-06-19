"""
URL configuration for pearlperfection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.views import *
from frontend.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msg/',message,name="msg"),
    path('product-form/',product,name='productform'),
    path('product/save',save_form,name="save"),
    path("product/table/",table,name="table"),
    path('delete/<int:dataid>/',delete,name="delete"),
    path("edit/<int:dataid>/",edit,name="edit"),
    path('register/',register_user,name="register"),
    path('',index,name="index"),
    path('products/',products,name="products"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact")
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

