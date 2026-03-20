from django.shortcuts import render

def home(request):
    return render(request, 'Q9/home.html')

def profile(request):
    return render(request, 'Q9/profile.html')

def contact(request):
    return render(request, 'Q9/contact.html')
