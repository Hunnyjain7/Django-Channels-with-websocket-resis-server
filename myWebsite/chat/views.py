from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.

def logIn(request):
    if request.session is None:
        return redirect('/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user.is_authenticated:
            request.session['id'] = user.id
            return redirect('/home')

    return render(request, 'login.html')


def home(request):
    try:
        if request.session['id']:
            return render(request, 'index.html')
    except Exception as E:
        e = E
        return redirect('/')
