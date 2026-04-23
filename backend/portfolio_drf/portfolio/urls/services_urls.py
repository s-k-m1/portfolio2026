from django.urls import path
from portfolio.views.services_views import service_list

urlpatterns = [
    path('', service_list, name='services-data'),
]