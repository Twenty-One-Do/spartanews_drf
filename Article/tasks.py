from celery import shared_task
from django.core.mail import send_mail
from SpartaNews import settings

from time import sleep

@shared_task
def send_alert(target_title, target_email, subject_username, subject_content):

    subject = f""" "{subject_username}"님께서 "{target_title}"에 답글을 달아주셨습니다. """
    message = f""" 
    "{target_title}"에 등록된 답글 

    - {subject_username}
    "{subject_content}"
    """
    to_email = [target_email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, to_email)
