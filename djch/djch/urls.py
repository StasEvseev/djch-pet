"""djch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import login, logout

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(('api.urls', 'api'))),
    path('chat/', include(('chat.urls', 'chat'))),

    path('accounts/login/', login, name='account_login'),
    path('accounts/logout/', logout, {'template_name': 'registration/logged_out1.html'}, name='account_logout'),

    path(r'docs/', include_docs_urls(title='My API title', public=False))
]
