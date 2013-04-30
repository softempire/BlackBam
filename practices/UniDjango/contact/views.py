from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def contactForm(request):
    c = {}
    # ...
    return render_to_response("contactForm.html", c,
                               context_instance=RequestContext(request))