from django.shortcuts import render
from django.http import HttpResponse

from .models import Tables

# Create your views here.
valid_columns=["Date" , "id" , "url" , "url_2" , "link_to_solicitation" , "agency" , "fsg" , "fsg_description" , "psc_code" , "PSC_description" , "source" , "title" , "keywords" , "email" , "phone" , "contract_specialist" , "contract_officer" , "set_aside" , "naics_code" , "contact_info" , "place_of_performance" , "description" , "Solicitation_Number" , "Notice_Type" , "Point_of_Contact" , "Point_of_Contact_email"]
list_item= [{"id1":"Hello","url":"world","id3":"test"},{"id1":"sainyam","id2":"Kapoor","agency":"test"},]
def populate():
    new_entry=Tables()
    for adict in list_item:
        for k in adict:
            if k in valid_columns:
                new_entry.url=adict[k]
                new_entry.save()


def index(request):
    # return HttpResponse('Hello from Python!')
    populate()
    return render(request, 'index.html')


def db(request):

    #greeting = Greeting()
    #greeting.save()

    #greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': "hello"})

