"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from post.views import index as posts_index
from shop.views import products_view, run_products_update
from blog.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_index, name='posts_index'),
    path('register/', register_view, name='register_view'),
    path('api/', include('api.urls', namespace='api')),
    path('', products_view, name='products_view'),
    path('run-task/', run_products_update, name='run_products_update'),
    path('django-rq/', include('django_rq.urls'))

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
