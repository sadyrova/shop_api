"""
URL configuration for shop_api project.

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
from django.urls import path
from django.conf.urls.static import static
from shop_api import settings

from product.views import hello_api_view, category_list_api_view, producty_list_api_view, review_list_api_view, category_retrieve_api_view, review_retrieve_api_view, producty_retrieve_api_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_api_view),
    path('api/category/', category_list_api_view),
    path('api/review/', review_list_api_view),
    path('api/producty/', producty_list_api_view),
    path('api/category/<int:id>/', category_retrieve_api_view),
    path('api/review/<int:id>/', review_retrieve_api_view),
    path('api/producty/<int:id>/', producty_retrieve_api_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
