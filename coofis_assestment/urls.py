"""
URL configuration for coofis_assestment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import create_document, submit_document, review_document, assign_reviewer


urlpatterns = [
    path('create/', create_document, name='create_document'),
    path('submit/<uuid:document_id>/', submit_document, name='submit_document'),
    path('review/<uuid:document_id>/', review_document, name='review_document'),
    path('assign-reviewer/<uuid:document_id>/', assign_reviewer, name='assign_reviewer'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('account/', include('apps.accounts.urls')),
    ]))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


