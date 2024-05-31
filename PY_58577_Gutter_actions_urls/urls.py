"""
URL configuration for PY_58577_Gutter_actions_urls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django_app.views import BookViewSet

router = DefaultRouter()
router.register(r'django_router/book/create/', BookViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('django_app/', include('django_app.urls')),
    path('django_app2/', include('django_app.urls')),
    path('django_app3/', include(router.urls)),
    path('custom_method/', BookViewSet.as_view({'get': 'custom_method'})),
]

urlpatterns += router.urls