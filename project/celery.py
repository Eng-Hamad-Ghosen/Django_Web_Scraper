from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# Set default Django settings module for Celery
# تعيين إعدادات Django الافتراضية
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# إنشاء مثيل Celery
app = Celery('project')

# Using a string here means the worker doesn't need to pickle the object
# تحميل إعدادات Celery من ملف الإعدادات الخاص بـ Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in Django apps
# اكتشاف المهام في التطبيقات المسجلة
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')