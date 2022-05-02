from django.shortcuts import render
from django.http import HttpResponse

import os
import time
import json
import sqlite3

dbconn = sqlite3.connect('/home/piserver/dev/webgarden/appDB.sqlite3')
mycursor = dbconn.cursor()

def getTemp():
    #import pdb; pdb.set_trace()
    sql = """SELECT temperature + 0E0, DATE_FORMAT(datetime,"%H:%i") FROM Temperature order by id desc LIMIT 120;"""
    mycursor.execute(sql)
    temps = mycursor.fetchall()
    mydb.commit()
    #temps = list(zip(*temps))
    return temps

def getImagePath():
    sql="""SELECT SUBSTRING(path,""" + str(cred['connection']['offset']) + """,65) FROM images ORDER by id desc LIMIT 1;"""
    mycursor.execute(sql)
    filename = mycursor.fetchall()[0][0]
    mydb.commit()
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
    return HttpResponse(" ".join(getTemp()[0]) + "\t" + getImagePath())

def update(request):
    #import pdb; pdb.set_trace()
    data = getTemp()
    jsonData = {"data":[]}
    for datum in data:
        jsonData["data"].append( {"temp":datum[0],"time":datum[1]} )

    return HttpResponse(json.dumps(jsonData))

def status(request):
    return HttpResponse("status page")

def schedule(request):
    return HttpResponse("schedule page")