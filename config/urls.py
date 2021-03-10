"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from users.api.urls import router as api_users
from projects.api.urls import router as api_projects
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


api_urls = [
    path('usuarios/', include(api_users.urls)),
    path('workspaces/', include(api_projects.urls)),
    path('token/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    # API
    path('api/', include(api_urls)),
]
