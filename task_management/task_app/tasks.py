from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from .models import Task

@shared_task
def send_task_assignment_email(user_email, task_title):
    send_mail(
        subject="New Task Assigned",
        message=f"You have been assigned a new task: {task_title}",
        from_email="admin@taskmanager.com",
        recipient_list=[user_email],
    )

@shared_task
def send_task_deadline_reminder():
    upcoming_tasks = Task.objects.filter(due_date__lte=now() + timedelta(days=1), status="pending")
    
    for task in upcoming_tasks:
        send_mail(
            subject="Task Deadline Reminder",
            message=f"Reminder: Your task '{task.title}' is due soon.",
            from_email="admin@taskmanager.com",
            recipient_list=[task.assigned_user.email],
        )
