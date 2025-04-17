# scraper/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from scraper.tasks import *

class SendBulkEmailsView(APIView):
    def post(self, request):
        email_list = request.data.get('emails', [])

        if not email_list:
            return Response({"error": "No emails provided"}, status=400)

        send_bulk_emails.delay(email_list)

        return Response({"message": "Email sending task has been scheduled!"}, status=200)