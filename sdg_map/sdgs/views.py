from django.shortcuts import render , redirect
from django.http import HttpResponse
import csv
from .froms import PartnerForm
from .models import Point

# Create your views here.

def index(request):
    points= Point.objects.all()
    context = {
        'points': points
    }
    
    return render(request,'index.html', context)

def add(request):
    print (request.POST)
    long = request.POST.get('longitude')
    lat = request.POST.get('latitude')
    added_p = Point.objects.create (
        Project_name= request.POST['Project_name'],
        area= request.POST['area'],
        partner_name= request.POST['partner_name'],
        sdgs=request.POST['sdg'],
        longitude=long,
        latitude=lat
    )
    added_p.save()
    
    return redirect('home')



def delete_point(request, point_id):
    try:
        point = Point.objects.get(id=point_id)
        point.delete()
    except Point.DoesNotExist:
        pass  
    return redirect('home')  

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="points.csv"'

    writer = csv.writer(response)
    writer.writerow(['Project Name', 'Partner Name', 'Area', 'SDGs'])

    points = Point.objects.all()
    for point in points:
        writer.writerow([point.Project_name, point.partner_name, point.area, point.sdgs])

    return response