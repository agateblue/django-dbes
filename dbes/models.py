# -*- coding: utf-8 -*-
from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Email(models.Model):
    recipient = models.EmailField(db_index=True)
    from_email = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    html_body = models.TextField(null=True, blank=True)
    plain_body = models.TextField(null=True, blank=True)
    subject = models.TextField()
    uuid = models.CharField(max_length=36, default=lambda: str(uuid4()), unique=True)

    @classmethod
    def from_message(cls, recipient, message):
        """create a model instance from a django.core.mail.message.EmailMultiAlternatives instance"""
        instance = cls(recipient=recipient, subject=message.subject, from_email=message.from_email)

        if message.content_subtype == 'html':
            missing_alternative = 'plain'
            instance.html_body = message.body
        elif message.content_subtype == 'plain':
            missing_alternative = 'html'
            instance.plain_body = message.body
        else:
            raise ValueError('You must provide either a HTML or a plain body to DBES backend')

        for body, mimetype in message.alternatives:
            if mimetype == 'text/{0}'.format(missing_alternative):
                setattr(instance, '{0}_body'.format(missing_alternative), body)
                break
        return instance

    def get_absolute_url(self):
        return reverse('dbes:email-detail', kwargs={'uuid': self.uuid})
