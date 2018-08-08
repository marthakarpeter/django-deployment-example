import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_proj.settings')
import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #create new webpage entry
        webpg = webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #create fake AccessRecord for that Webpage
        #name is the entire webpage because it is a ForeignKey in the models.py
        acc_recc = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='main':
    print('populating script')
    populating(20)
    print('populating complete')
