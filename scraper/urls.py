from django.urls import path
from scraper.views import *

urlpatterns = [
    path('send-bulk-emails/', SendBulkEmailsView.as_view(), name='send_bulk_emails'),
    path('test/', test, name='test'),
]