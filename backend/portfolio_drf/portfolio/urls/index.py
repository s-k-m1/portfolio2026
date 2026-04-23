from django.urls import path, include

urlpatterns = [
    path('about/', include('portfolio.urls.about_urls')),
    path('services/', include('portfolio.urls.services_urls')),
]