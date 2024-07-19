# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import AssignmentDetails
from datetime import date

@receiver(post_save, sender=AssignmentDetails)
def send_urgent_task_email(sender, instance, created, **kwargs):
    if instance.end_date <= date.today():
        # Compose email
        subject = 'Urgent Task Notification'
        message = f'Task "{instance.task}" is due on {instance.end_date}. Please take action immediately.'
        recipient_list = ['dhruvatej6565@gmail.com']  # Replace with actual farmer email address
        sender_email = 'workdhruvateja@gmail.com'  # Replace with the sender email address

        # Send email
        send_mail(
            subject,
            message,
            sender_email,
            recipient_list,
            fail_silently=False,
        )

