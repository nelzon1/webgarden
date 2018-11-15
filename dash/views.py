from django.shortcuts import render
from django.http import HttpResponse
import os
import time

def getTemp():
    #import pdb; pdb.set_trace()
    filename = os.path.join(os.getcwd(),"proc","tempdata","")
    now = time.localtime()
    timestr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    filename += timestr + ".dat"
    temps = []
    data_points = 20
    try:
        with open(filename,'r') as data:
            raw = [ list(x.split(',')) for x in  data.read().splitlines() ]
            if len(raw) < data_points:
                temps = raw
            else:
                temps = raw[-data_points:]
    except FileNotFoundError:
        print('File not found: ' + filename)

    return temps

def getImagePath():
    
    now = time.localtime()
    timestr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    filename = os.path.join(os.getcwd(),"dash","static","dash","images", timestr )
    try:
        files = os.listdir(filename)
        files = sorted(files)
        filename = os.path.join("dash","images",timestr,files[-1])
    except FileNotFoundError:
        print("Directory not found: " + filename)   
    return filename


# Create your views here.
def home(request):
    context = {
        'title': 'WebGarden'
    }
    #import pdb; pdb.set_trace()
    return render(request, 'dash/home.htm', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    #import pdb; pdb.set_trace()
    return HttpResponse(" ".join(getTemp()) + "\t" + getImagePath())
