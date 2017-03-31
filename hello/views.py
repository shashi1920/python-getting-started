from django.shortcuts import render
from django.http import HttpResponse

from .models import Tables

# Create your views here.
valid_columns=["Date" , "id" , "url" , "url_2" , "link_to_solicitation" , "agency" , "fsg" , "fsg_description" , "psc_code" , "PSC_description" , "source" , "title" , "keywords" , "email" , "phone" , "contract_specialist" , "contract_officer" , "set_aside" , "naics_code" , "contact_info" , "place_of_performance" , "description" , "Solicitation_Number" , "Notice_Type" , "Point_of_Contact" , "Point_of_Contact_email"]
def populate():
    list_item = [{"naics_code": "8258", "url": "world", "id3": "test"},
                 {"id1": "sainyam", "id2": "Kapoor", "agency": "test"}, ]
    new_entry=Tables()
    for adict in list_item:
        for k in adict:
            if k in valid_columns:
                if k!='naics_code':
                    setattr(new_entry,k,adict[k])
                else:
                    setattr(new_entry,k,int(adict[k]))
                #new_entry.url=adict[k]
                new_entry.save()



def index(request):
    # return HttpResponse('Hello from Python!')
    populate()
    print_demo=Tables.objects.all()


    return render(request, 'index.html',context={"printd":print_demo})



def db(request):

    #greeting = Greeting()
    #greeting.save()

    #greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': "hello"})

