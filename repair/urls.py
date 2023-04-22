from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('root-admin/', admin.site.urls),
    path('log/', include('log.urls')),
    path('', RedirectView.as_view(url='log/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/', include('staff.urls')),
]

urlpatterns += static(
  settings.MEDIA_URL, 
  document_root=settings.MEDIA_ROOT
)