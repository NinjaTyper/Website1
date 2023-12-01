from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def home(request):
    content = "<html><body><h1>this is some testing</h1></body></html>"
    return HttpResponse(content)

def login(request):
    logindata = "<html><body><h1>LOGIN RIGHT NOW</h1></body></html>"
    return HttpResponse(logindata)

def display_date(request):
    date_month = datetime.today().month
    date_day = datetime.today().day
    date_year = datetime.today().year
    today_date = str(date_month) + "/" + str(date_day) +"/" + str(date_year)
    return HttpResponse(today_date)
