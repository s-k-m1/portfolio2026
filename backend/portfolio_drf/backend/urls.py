from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

# A simple view to confirm the backend is live
def health_check(request):
    return JsonResponse({
        "status": "online",
        "message": "SKM Portfolio Backend is running",
        "timezone": "Asia/Kathmandu"
    })

urlpatterns = [
    # Root URL - Fixes the 404 error
    path('', health_check),
    
    path('admin/', admin.site.urls),
    path('api/portfolio/', include('portfolio.urls.index')),
    path('accounts/', include('accounts.urls')), 
]

# Essential for serving images/media in development and production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)