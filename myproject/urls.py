"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from myapp.views import home,vendor_list,vendor_detail,categories_by_location,category_detail,subcategory_page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="category_list"),
    path("search/", vendor_list, name="vendor_list"),
    path("vendor/<slug:slug>/", vendor_detail, name="vendor_detail"),
    path("categories/", categories_by_location, name="category_by_location"),
    path("category/<slug:slug>/", category_detail, name="category_detail"),
    path("subcategory/<slug:slug>/", subcategory_page, name="subcategory_page"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
