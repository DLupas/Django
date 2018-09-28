from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

def events(request):
    return HttpResponse('The following events will happen')


