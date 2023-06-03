from django.shortcuts import render, HttpResponse,redirect
from time import gmtime, strftime
    
def showtime(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %S %p", gmtime())
    }
    return render(
        request,
        'index.html',
        context)
