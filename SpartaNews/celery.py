from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# Django 프로젝트의 settings 모듈을 Celery에게 알려줍니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SpartaNews.settings')

app = Celery('SpartaNews')

# namespace='CELERY'는 Celery 관련 설정을 Django의 설정 파일에서 가져오게끔 합니다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 등록된 Django 앱 구성에서 task 모듈을 자동으로 찾아냅니다.
app.autodiscover_tasks()