from django.urls import path
from portfolio.views.about_views import AboutDataView

urlpatterns = [
    path('', AboutDataView.as_view(), name='about-data'),
]