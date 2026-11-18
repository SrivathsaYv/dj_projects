from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def moving_text(request):
    return HttpResponse("<marquee>Hello All</marquee>")