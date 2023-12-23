from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.template import loader

def home(request):
    content = "<html><body><h1>this is some testing</h1></body></html>"
    return HttpResponse(content)

def login(request):
    template = loader.get_template("login/login.html")
    return HttpResponse(template.render())

def display_date(request):
    date_month = datetime.today().month
    date_day = datetime.today().day
    date_year = datetime.today().year
    today_date = str(date_month) + "/" + str(date_day) +"/" + str(date_year)
    return HttpResponse(today_date)

def about(request):
    about_content = {'about' : "This website is made by Peter, Phu, Luigi. Peter is a 12 year old boy who spends far too much time on typing"}
    return render(request, "about.html", about_content)
