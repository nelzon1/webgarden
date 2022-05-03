from django.shortcuts import render
from django.http import HttpResponse

import os
import time
import json
import sqlite3

creds = {}
with (open('./proc/dbinfo.json','r') as options):
    creds = json.loads(options.read())



def getTemp():
    dbconn = sqlite3.connect(creds['dbPath'])
    mycursor = dbconn.cursor()
    #import pdb; pdb.set_trace()
    sql = """SELECT temperature, datetime FROM Temperature order by TemperatureID desc LIMIT 360;"""
    temps = list(mycursor.execute(sql))
    #temps = list(zip(*temps))
    dbconn.close()
    return temps

def getImagePath():
    dbconn = sqlite3.connect(creds['dbPath'])
    mycursor = dbconn.cursor()
    sql="""SELECT SUBSTRING(path,""" + str(cred['connection']['offset']) + """,65) FROM images ORDER by id desc LIMIT 1;"""
    mycursor.execute(sql)
    filename = mycursor.fetchall()[0][0]
    dbconn.close()
    return filename


# Create your views here.
def home(request):
    context = {
        'title': 'WebGarden',
        'imagePath': 'blah' #getImagePath()
    }
    #import pdb; pdb.set_trace()
    return render(request, 'dash/home.htm', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    #import pdb; pdb.set_trace()
    #return HttpResponse(" ".join(getTemp()[0]) + "\t" + getImagePath())
    return HttpResponse("\n".join(str(getTemp()[0])))

def update(request):
    #import pdb; pdb.set_trace()
    data = getTemp()
    jsonData = {"data":[]}
    for datum in data:
        jsonData["data"].append( {"temp":datum[0],"time":datum[1][-8:-3]} )

    return HttpResponse(json.dumps(jsonData))

def status(request):
    return HttpResponse("status page")

def schedule(request):
    return HttpResponse("schedule page")
