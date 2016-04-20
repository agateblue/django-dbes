# -*- coding: utf-8 -*-
from uuid import uuid4
import logging

from django.dispatch import receiver
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
    uuid = models.CharField(max_length=36, default=uuid4, unique=True)

    class Meta:
        ordering = ('-creation_date',)

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

        for body, mimetype in getattr(message, 'alternatives', []):
            if mimetype == 'text/{0}'.format(missing_alternative):
                setattr(instance, '{0}_body'.format(missing_alternative), body)
                break
        return instance

    def get_absolute_url(self):
        return reverse('dbes:email-detail', kwargs={'uuid': self.uuid})

@receiver(models.signals.post_save, sender=Email)
def log_email(sender, instance, created, **kwargs):
    if not created:
        return

    logger = logging.getLogger('django')
    logger.info('Sending email to {0} with subject "{1}". You can access this email at URL {2}'.format(
        instance.recipient,
        instance.subject,
        instance.get_absolute_url()
    ))
