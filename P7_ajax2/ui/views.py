from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def edit_heading(request):
    import datetime
    now = datetime.datetime.now()
    return JsonResponse({'heading': f'{now}'})