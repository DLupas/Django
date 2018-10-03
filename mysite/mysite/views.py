from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    #return HttpResponse('Hello World')
    return render(request, 'mysite/home.html')
    #template = loader.get_template('home.html')
#    return HttpResponse(template.render(request))

def events(request):
    #return HttpResponse('The following events will happen')
    return render(request, 'events.html')
