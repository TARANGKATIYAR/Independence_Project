from django.shortcuts import render, HttpResponse
from backendsite.models import Contact
from datetime import datetime
# Create your views here.
def index(request): 
    return render(request, "index.html")

def copyright(request):
    return render(request, "copyright.html")

def sent(request):
    if request.method == "GET":
        name = request.GET.get("name")
        email = request.GET.get("email")
        message = request.GET.get("message")

        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()

    return render(request, "done.html")