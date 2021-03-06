"""workforceAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from workforceAPI import views
from workforceAPI import auth_views

urlpatterns = [
    path('api', views.root),
    path('api/models', views.models),
    path('api/models/<str:model_id>', views.get_model),
    path('api/share_model', views.share_model),
    path('api/delete_model', views.delete_model),
    path('api/file-upload', views.file_upload),
    path('api/rerun-model', views.rerun_model),

    path('api/whoami', auth_views.whoami),
    path('api/login', auth_views.login),
    path('api/logout', auth_views.logout),
    path('api/authorize', auth_views.authorize),
]
