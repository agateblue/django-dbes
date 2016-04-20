#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-dbes
------------

Tests for `django-dbes` models module.
"""

from django.test import TestCase
from django.utils import timezone

from dbes import models


class TestDbes(TestCase):

    def setUp(self):
        pass

    def test_email_creation(self):
        now = timezone.now()
        email = models.Email(recipient='test@test.com', subject='test', html_content='test')

        self.assertGreater(email.creation_date, now)

    def tearDown(self):
        pass
