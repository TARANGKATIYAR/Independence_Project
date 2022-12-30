from django.shortcuts import render, HttpResponse
from backendsite.models import Contact, Messages
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

def comment(request):
    context = {'display': 'none', "messages_list": Messages.objects.order_by('id')}


    if request.method == "POST":
        person_name = request.POST.get('person', 'None')
        comment = request.POST.get('comment', 'None')
        if person_name == 'None' and comment == "None":
            pass
        else:
            message_instance = Messages.objects.create(name=person_name, comment=comment)
            context['display'] = "block"
            context['message_list'] = Messages.objects.order_by('id')


    return render(request, 'comment.html', context)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)