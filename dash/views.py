from django.shortcuts import render
from django.http import HttpResponse
import os
import time
import json
import mysql.connector

global cred

with open('proc/dbinfo.json','r') as json_file:
    cred = json.load(json_file)

mydb = mysql.connector.connect(
        host=cred['connection']['host'],
        user=cred['connection']['user'],
        passwd=cred['connection']['pwd'],
        database=cred['connection']['database'],
        port=cred['connection']['port']
        )

mycursor = mydb.cursor()

def getTemp():
    #import pdb; pdb.set_trace()
    sql = """SELECT temperature + 0E0, DATE_FORMAT(datetime,"%H:%i:%s") FROM temperature LIMIT 20;"""
    mycursor.execute(sql)
    temps = mycursor.fetchall()
    temps = list(zip(*temps))
    return temps

def getImagePath():
    
    sql="""SELECT SUBSTRING(path,13,65) FROM images ORDER by id desc LIMIT 1;"""
    mycursor.execute(sql)
    filename = mycursor.fetchall()[0][0]

    return filename


# Create your views here.
def home(request):
    tempData = getTemp()
    temps = "[" + ",".join([str(x) for x in tempData[0]]) + "]"
    times = '["' + '","'.join(tempData[1]) + '"]'
    context = {
        'title': 'WebGarden',
        'imagePath': getImagePath(),
        'temps':temps,
        'times':times
    }
    #import pdb; pdb.set_trace()
    return render(request, 'dash/home.htm', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    #import pdb; pdb.set_trace()
    return HttpResponse(" ".join(getTemp()[0]) + "\t" + getImagePath())
