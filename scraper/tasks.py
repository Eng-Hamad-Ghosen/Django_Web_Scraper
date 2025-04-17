import time
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_bulk_emails(email_list):
    subject = 'Hello from Hamad!'
    message = 'This is a bulk email sent using Celery and Django.'
    from_email = 'Hamad@gmail.com'

    for email in email_list:
        try:
            send_mail(subject, message, from_email, [email])
            print(f"Email sent to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {str(e)}")

@shared_task
def send_email_task(email):
    # email = '***ABC123***'
    print(f'Sending email to {email}')
    time.sleep(5)  # Simulate sending email
    print('Email sent successfully!')
    return "Email Sent"


@shared_task
def send_scheduled_emails():
    pass