from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('result/', ResultView.as_view(), name='result'),
    path('search_help', search_view, name='search_help'),
    path('game_report/', ReportView.as_view(), name='report')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
