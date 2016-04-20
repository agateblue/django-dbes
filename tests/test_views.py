#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.test import TestCase, override_settings
from django.utils import timezone
from django.core import mail

from dbes import models

@override_settings(EMAIL_BACKEND='dbes.backends.EmailBackend')
class TestDbes(TestCase):

    def test_can_display_txt_email_in_view(self):
        mail.send_mail('subject', 'message', 'from@from.com', ['to1@to.com'])

        e = models.Email.objects.get(recipient='to1@to.com')
        url = e.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertHTMLEqual(response.content.decode('utf-8'), 'message')

    def test_can_display_html_email_in_view(self):
        mail.send_mail('subject', 'message', 'from@from.com', ['to1@to.com'], html_message='<strong>message</strong>')

        e = models.Email.objects.get(recipient='to1@to.com')
        url = e.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertHTMLEqual(response.content.decode('utf-8'), '<strong>message</strong>')
