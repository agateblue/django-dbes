# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from uuid import uuid4


class Email(models.Model):
    recipient = models.EmailField(db_index=True)
    creation_date = models.DateTimeField(default=timezone.now)
    html_content = models.TextField()
    subject = models.TextField()
    uuid = models.CharField(max_length=36, default=lambda: str(uuid4()))
