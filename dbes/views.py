from django.views import generic
from django.http import Http404

from . import models


class EmailDetail(generic.DetailView):
    template_name = 'dbes/detail.html'
    context_object_name = 'email'
    
    def get_object(self, queryset=None):
        try:
            return models.Email.objects.get(uuid=self.kwargs['uuid'])
        except models.Email.DoesNotExist:
            raise Http404
