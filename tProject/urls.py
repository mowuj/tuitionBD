
from django.contrib import admin
from django.urls import path,include
from tuition import views
from .views import *
from tuition.views import ContactView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='HomeView'),
    # path('contact',ContactView.as_view(),name='contact'),
    # path('', TemplateView.as_view(template_name='home.html'), name='HomeView'), 
    path('tuition/', include('tuition.urls')),
    path('session/', include('session.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
