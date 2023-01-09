import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Core.settings')
# import random
from random import randrange

import django 
django.setup()
import requests
from django.contrib.auth.models import User

from faker import Faker
from pprint import pprint
from kitablar.api.serializers import KitabSerializer
def set_user():
    fake = Faker(['az_AZ'])
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name().lower()}"
    # print(f_name,l_name,u_name,email)


    user_check = User.objects.filter(username=u_name) 
    while user_check.exists():
        u_name = u_name + str(randrange(100,1000))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email = email
        )

    user.set_password("Passw0rd#")
    user.save()


def kitab_elave_et(movzu):
    fake = Faker(['az_AZ'])
    # url = f"https://openlibrary.org/search.json?q={movzu}"
    # response = requests.get(url)
    url = "https://openlibrary.org/search.json"
    payload = {
        'q':movzu
    }
    response = requests.get(url,params=payload)
    # print(response.url)
    if response.status_code != 200:
        print("Bad request",response.status_code)
        return 
    if response.status_code == 200:
        response_json = response.json()
        respons_item = response_json.get("docs")
        for k in respons_item:
            data = dict(
                ad = k.get("title"),
                muellif = k.get("author_name")[0],
                izah = "Lorem Ipsum Dolor Sit Amet.",
                paylasildi = fake.date_time_between(start_date="-10y",end_date="now",tzinfo=None)
            )
            # pprint(data)
            serializer = KitabSerializer(data=data)
            # pprint(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("Olmadı")
                continue