from django.shortcuts import render

def index(request):
    return render(request, 'guestbook/index.html')

def cropselection(request):
    return render(request, 'guestbook/cropselection.html')

def signup(request):
    return render(request, 'guestbook/signup.html')

def login(request):
    return render(request, 'guestbook/login.html')

def feedback(request):
    return render(request, 'guestbook/feedback.html')

def state(request):
    return render(request, 'guestbook/state.html')

def sugarcanefarming(request):
    return render(request, 'guestbook/sugarcanefarming.html')

def statecrop(request):
    return render(request, 'guestbook/statecrop.html')