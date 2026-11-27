from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import models
from django.views.decorators.csrf import csrf_exempt
Error = False
# Create your views here.
def home(request):
    return render(request,'index.html')

@csrf_exempt
def register(request):
    user = request.POST.get('username')
    pwd = request.POST.get('pwd')
    print(request.POST, 55555)
    global Error
    if not Error:
        Error = not Error
        models.User.objects.create_user(username=user, password=pwd)
        return JsonResponse({'status': f'Account({user}) Created'})
    else:
        Error = not Error
        return JsonResponse({'status': 'wrong try'}, status=501 )