from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
    
    # my_dict = {'insert_me':'i am from views.py truckindex.html',}
    # return render(request,'first_app/truckindex.html',context=my_dict)
