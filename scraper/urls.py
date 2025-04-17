from django.urls import path
from scraper.views import SendBulkEmailsView

urlpatterns = [
    path('send-bulk-emails/', SendBulkEmailsView.as_view(), name='send_bulk_emails'),
]