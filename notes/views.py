from django.http import HttpResponse



def greeting(request):
    html = "<h1>Hello from Notes app.</h1>"
    return HttpResponse(html)