from django.shortcuts import render

# Create your views here.
def add_contact(request):
    if request.method == 'GET':
        return render(request, 'add_contact.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')

        # Save the contact to the database
        from .models import Contact
        contact = Contact(name=name, email=email, birthday=birthday)
        contact.save()

        return render(request, 'message.html', {'message': 'Contact added successfully!'})