from django.core.mail.backends.base import BaseEmailBackend
from .models import Email

class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        return len(self.create_email_model_instances(email_messages))
        
    def create_email_model_instances(self, email_messages):
        instances = [Email.from_message(recipient, message) for message in email_messages for recipient in message.recipients()]
        Email.objects.bulk_create(instances)
        return instances
