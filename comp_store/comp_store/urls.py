from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView
from django.views.generic import    TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('login/', include('oauth.urls')),
    path('', include('comps.urls')),
    path('api/v1/', include('routers')),
    path('logout/', LogoutView.as_view()),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home1'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)