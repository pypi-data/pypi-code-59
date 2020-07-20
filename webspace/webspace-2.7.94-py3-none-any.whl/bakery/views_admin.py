import logging
from django.http import HttpResponse
from django.shortcuts import render

from webspace.cms import constants
from webspace.bakery.celery import bakery_build, app

logger = logging.getLogger('bakery')


def index(request):
    return render(
        request,
        '%s/bakery.html' % constants.ADMIN_TEMPLATES_PATH,
        {'cache_icon': 'cog'}
    )


last_id = 'None'


def build(request):
    """
    from django.core.cache import caches
    if 'last_id' in caches:
        task = app.AsyncResult(last_id)
        if task.ready():
            task = bakery_build.delay()
            caches['last_id'] = task.id
            return HttpResponse("Build is running !")
        return HttpResponse("Build is already running !")
    else:
        task = bakery_build.delay()
        caches['last_id'] = task.id
    """
    return HttpResponse("Build is running !")
