from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 Auth system (login/logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Blog URLs
    path('', include('blog.urls')),
]

# 📸 Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)