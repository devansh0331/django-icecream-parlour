from django.contrib import admin
from django.urls import path , include
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path("" , views.index , name="home"),
    path("about" , views.about , name="about"),
    path("services" , views.services , name="services"),
    path("contact" , views.contact , name="contact"),
    
]
