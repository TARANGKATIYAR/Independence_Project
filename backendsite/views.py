from django.shortcuts import render, HttpResponse
from backendsite.models import Contact, Messages, Padlet
from datetime import datetime
# Create your views here.
def index(request): 
    context = {'padlet_list': Padlet.objects.order_by('id')}
    return render(request, "index.html", context)

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

def padlet(request):
    

    if request.method == "GET":
        name = request.GET.get('name', 'None')
        subject = request.GET.get('subject', 'None')
        mycomment = request.GET.get('mymessage', 'None')
        if name == 'None' and subject == 'None' and mycomment == 'None':
            pass
        else: 
            padlet_instance = Padlet.objects.create(name=name, subject=subject, message=mycomment)
            padlet_instance.save()

    return render(request, 'padlet.html')

def page_not_found_view(request, exception): 
    return render(request, '404.html', status=404)
