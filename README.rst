===========================================
django-dbes (Django Database Email Storage)
===========================================

.. image:: https://badge.fury.io/py/django-dbes.png
    :target: https://badge.fury.io/py/django-dbes

.. image:: https://travis-ci.org/EliotBerriot/django-dbes.png?branch=master
    :target: https://travis-ci.org/EliotBerriot/django-dbes

A django package to speed-up your HTML email development workflow in django.

**Warning**: this package is intended for development only.

Use case
--------

Working on email templates/styling in django can be really painful and slow:

* Dumping the email content to console via django's `ConsoleBackend` is just not enough when you work with HTML emails
* Sending the emails to a real adress is slow, requires a working SMTP server, and may be dangerous. It will also quickly spam your inbox.

A possible answer
-----------------

What if we could display sent emails directly in browser during development ? It's actually quite simple, and it's exactly
what ``django-dbes`` does:

1. Instead of sending mails or logging them to console, they're stored as model instances in the database
2. The email URL is logged on the console so it can be accessed it in a web browser
3. The view behind this URL retrieves the model instance and renders its content in a template

The project is also bundled with an admin module so you can quickly see what the last sent emails were and display them.

Quickstart
----------

Install ``django-dbes``::

    pip install django-dbes

Then add the app to your settings.py::

    INSTALLED_APPS = [
        # other apps
        'dbes',
    ]

    EMAIL_BACKEND = 'dbes.backends.EmailBackend'

Add this to your URLs conf::

    urlpatterns = [
        # your urls
        url(r'^emails/', include('dbes.urls', namespace='dbes')),
    ]

Run the migrations::

    python manage.py migrate dbes

From now on, each time you send an email, it will be saved as a model instead of being sent. You'll also see
a log output in your console, such as:

    Sending email to contact@test.com with subject "Test". You can access this email at URL http://127.0.0.1:8000/emails/8b2b0bf2-bfb3-4771-a14c-f6d4dc9a635b

Just click the email link to display it.


Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
