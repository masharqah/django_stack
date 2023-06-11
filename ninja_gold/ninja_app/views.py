from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
    if "gold" not in request.session :
        request.session['gold']=int(0)
        request.session['tracker']=[]  
    return render (request, "index.html")

def setparameters(request):
    request.session['target']=int(request.POST['target'])
    request.session['counter']=int(request.POST['counter'])
    return redirect('/')

def reset(request):
    request.session['counter']=int(0)
    request.session['target']=int(0)
    request.session['gold']=int(0)
    request.session['tracker']=[]
    return redirect ('/')

def proccess_money(request):

    if request.POST['building'] == 'farm':
        amount=random.randint(10,20)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.POST['building']} at {logger} "
    
    elif request.POST['building'] == 'cave':
        amount=random.randint(5,10)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.POST['building']} at {logger} "

    elif request.POST['building'] == 'house':
        amount=random.randint(2,5)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.POST['building']} at {logger} "

    elif request.POST['building'] == 'casino':
        amount=random.randint(-50,50)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        if amount < 0 :
            trackMessage = f"you lost {amount} from {request.POST['building']} at {logger} Gambler!"
        elif amount > 0 :
            trackMessage = f"you earned {amount} from {request.POST['building']} at {logger} "
        elif amount == 0 :
            trackMessage = f"{request.POST['building']} is not giving neither taking from you ...{logger} "
    
    request.session['tracker'].insert(0,trackMessage)
    request.session["gold"]+=amount
    request.session['counter'] -= 1

    return redirect ('/')
