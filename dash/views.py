from django.shortcuts import render
from django.http import HttpResponse

import os
import time
import json
import sqlite3

creds = {}
with (open('./proc/dbinfo.json','r') as options):
    creds = json.loads(options.read())



def getTemp(params):
    # temp every minute, days = 12 * 60 minutes
    #import pdb; pdb.set_trace()
    if 'days' in params:
        if int(params['days'][0]) == -1:
            limit = 1000000
        elif int(params['days'][0]) == 0:
            limit = 360
        else:
            limit = int(params['days'][0]) * 60 * 24
    else:
        limit = 360
    dbconn = sqlite3.connect(creds['dbPath'])
    mycursor = dbconn.cursor()
    #
    sql = """SELECT temperature, datetime FROM Temperature order by TemperatureID desc LIMIT {limit};"""
    sql = sql.format(limit=limit)
    #print(sql)
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
        'imagePath': 'dash/images/qualityPicture.jpg', #getImagePath()
        'imageList': getImageList()
    }
    #import pdb; pdb.set_trace()
    return render(request, 'dash/home.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    #import pdb; pdb.set_trace()
    #return HttpResponse(" ".join(getTemp()[0]) + "\t" + getImagePath())
    return HttpResponse("\n".join(str(getTemp()[0])))

def update(request):
    #import pdb; pdb.set_trace()
    params = dict(request.GET)
    #print(request.GET)
    data = getTemp(params)
    jsonData = {"data":[]}
    for datum in data:
        jsonData["data"].append( {"temp":datum[0],"time":datum[1][-8:-3]} )

    return HttpResponse(json.dumps(jsonData))

def status(request):
    return HttpResponse("status page")

def schedule(request):
    return HttpResponse("schedule page")

def getImage(request):
    #valid_image = getImagePath()
    valid_image = './proc/LatestImage.jpg'
    try:
        with open(valid_image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
 
def getImageList():
    from os.path import isfile, join
    imagePath = creds['serverPath'] + '/proc/imgArchive/'
    onlyfiles = [f for f in os.listdir(imagePath) if isfile(join(imagePath, f))]
    onlyfiles += ['Latest Image','Quality Image']
    return onlyfiles