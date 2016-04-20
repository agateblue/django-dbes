import logging
logger = logging.getLogger('django')

def log_email(email):
    logger.info('Sending email to {0} with subject "{1}". You can access this email at URL {2}'.format(
        email.recipient,
        email.subject,
        email.get_absolute_url()
    ))
