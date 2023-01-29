from django.shortcuts import render

# Create your views here.
from app1.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    
    QSW=Webpage.objects.filter(name__startswith='M')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')    
    QSW=Webpage.objects.filter(name__regex='\w{3}')
    QSW=Webpage.objects.filter(name__in=['siva','MSD','RAMA'])
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='siva'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='volley ball') & Q(url__startswith='https'))
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)
    
def display_access(request):
    
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2022-08-10')    
    QSA=AccessRecords.objects.filter(date__gt='2022-08-10')    
    QSA=AccessRecords.objects.filter(date__gte='2022-08-10') 
    QSA=AccessRecords.objects.filter(date__lte='2023-08-10')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2022')  
    QSA=AccessRecords.objects.filter(date__month='9')    
    QSA=AccessRecords.objects.filter(date__day='18')   
    QSA=AccessRecords.objects.filter(date__year__gt='2022')
    d={'access':QSA}
    return render(request,'display_Access.html',d)
