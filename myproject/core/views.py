from decouple import config
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django_celery_results.models import TaskResult

from .tasks import print_numbers


def index(request):
    template_name = 'index.html'
    object_list = TaskResult.objects.all()
    my_key = config('KEY')
    context = {'object_list': object_list, 'my_key': my_key}
    return render(request, template_name, context)


def run_task(request):
    print_numbers.delay(10)
    url = 'core:index'
    return HttpResponseRedirect(reverse(url))
