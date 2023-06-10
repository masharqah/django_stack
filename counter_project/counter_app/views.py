from django.shortcuts import render, redirect

def index(request):
    count=request.session.get('counter', 0)
    
    if request.method == 'POST':
        if 'increment' in request.POST:
            increment = int(request.POST.get('increment'))
            count += increment
            request.session['counter'] = count
        elif 'reset' in request.POST:
            count = 0
            request.session['counter'] = count
        return redirect('/')

    return render(request, 'index.html', {'count': count})
