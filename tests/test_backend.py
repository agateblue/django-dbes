#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.test import TestCase, override_settings
from django.utils import timezone
from django.core import mail

from dbes import models

@override_settings(EMAIL_BACKEND='dbes.backends.EmailBackend')
class TestDbes(TestCase):

    def setUp(self):
        pass

    def test_email_plain_creation(self):
        recipients = [
            'to1@to.com',
            'to2@to.com',
        ]
        mail.send_mail('subject', 'message', 'from@from.com', recipients)
        for r in recipients:
            e = models.Email.objects.get(recipient=r)
            self.assertEqual(e.subject, 'subject')
            self.assertEqual(e.from_email, 'from@from.com')
            self.assertEqual(e.plain_body, 'message')
            self.assertEqual(e.html_body, None)

    def test_email_html_creation(self):
        recipients = [
            'to1@to.com',
            'to2@to.com',
        ]
        mail.send_mail('subject', 'message', 'from@from.com', recipients, html_message='<strong>message</strong>')
        for r in recipients:
            e = models.Email.objects.get(recipient=r)
            self.assertEqual(e.subject, 'subject')
            self.assertEqual(e.from_email, 'from@from.com')
            self.assertEqual(e.html_body, '<strong>message</strong>')
            self.assertEqual(e.plain_body, 'message')


    def tearDown(self):
        pass
