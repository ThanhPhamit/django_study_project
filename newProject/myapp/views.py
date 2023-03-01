from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import LogForm
from .models import  Person
from django.views.generic.list import ListView
# Create your views here.

class PeopleView(ListView):
    template_name = "people.html"
    model = Person

def home(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")


def menu(request):
    text = "<h1>Django documentation</h1>"
    return HttpResponse(text)


def index(request: HttpRequest):
    path = request.path
    method = request.method
    schema = request.scheme
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    content = f""" <center>
        <h2>Testing Django Request Response Objects</h2> 
        <p>Request path : " {path}</p> 
        <p>Request method :{method}</p>
        <p>Request schema :{schema}</p>
        <p>Request address :{address}</p>
        <p>Request user agent :{user_agent}</p>
        <p>Request path info :{path_info}</p>
        <p>Request header :{response.headers}</p>
    </center> """
    # return HttpResponse(content, content_type='text/html', charset='utf-8')
    return HttpResponse(content=content)


def menu_item(request: HttpRequest, dish):
    items = {
        'pasta': "a dish originally from Italy consisting of dough made from durum wheat, extruded or stamped into various shapes and cooked in boiling water, and typically served with a sauce.",
        'cheese': "a food made from the pressed curds of milk.",
        'hamburger': "a round patty of ground beef, fried or grilled and typically served on a bun or roll and garnished with various condiments."
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)


def get_num(request: HttpRequest, num):
    return HttpResponse(f"<h2>{num}</h2>")


def login_form_view(request: HttpRequest):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form,
               "header": "Welcome to softworld!",
               "user": "admin",
               "list": [
                   {'name': "falafel", 'old': "12"},
                   {'name': "shawarma", 'old': "15"},
                   {'name': "gyro", 'old': "10"},
                   {'name': "thanh", 'old': "10"},
               ]}
    return render(request, "home.html", context)

def people(request: HttpRequest):
    people = Person.objects.all()
    context = {'people' : people}
    return render(request, "people.html", context)
