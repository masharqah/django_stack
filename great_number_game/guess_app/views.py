from django.shortcuts import render, redirect
import random

def index(request):
    return render (request, 'index.html')

def guess (request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)

    if request.method == 'POST':
        guess = int(request.POST['guess'])
    if guess < request.session['number']:
        request.session['message'] = 'Too low!'
    elif guess > request.session['number']:
        request.session['message'] = 'Too high!'
    else:
        request.session['message'] = 'Congratulations! You guessed the correct number!'
        request.session.pop('number')   
    return redirect('/')