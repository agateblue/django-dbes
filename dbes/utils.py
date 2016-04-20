import logging
logger = logging.getLogger('django')

from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

def log_email(email):
    request = None
    protocol = getattr(settings, 'HTTP_PROTOCOL', 'http')
    full_url = ''.join([protocol, '://', get_current_site(request).domain, email.get_absolute_url()])
    logger.info('Sending email to {0} with subject "{1}". You can access this email at URL {2}'.format(
        email.recipient,
        email.subject,
        full_url
    ))
