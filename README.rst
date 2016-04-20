=============================
django-dbes
=============================

.. image:: https://badge.fury.io/py/django-dbes.png
    :target: https://badge.fury.io/py/django-dbes

.. image:: https://travis-ci.org/EliotBerriot/django-dbes.png?branch=master
    :target: https://travis-ci.org/EliotBerriot/django-dbes

A django app to store sent emails in database, for developement purpose. It's bundled with an EmailBackend that
save emails in database instead of actually sending them. You can then display each email using a unique URL
to debug your HTML and CSS.

An admin is provided to conveniently speed up your workflow.

Quickstart
----------

Install django-dbes::

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

From now on, each time you send an email, it will be saved as a model instead of being sent.

Features
--------

* TODO

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
