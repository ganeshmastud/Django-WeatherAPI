from django.shortcuts import render, redirect
import requests
# Create your views here.
from .models import City
def index(request):
    if request.method =='POST':
        city = request.POST['search']

        print("your search:",city)
        url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=68a5f10c3ab0b551d1c6f5d33dd448ea'

        r=requests.get(url.format(city)).json()
        print(r)
        if len(city)==0:
            all_cities = City.objects.all()#.order_by('id')[::-1]

            context={
                'message':'please enter something to search.',
                'msg':'alert alert-danger',
                'all_cities':all_cities

            }
            return render(request,'index.html',{'context':context})
        if 'message' in r:
            all_cities = City.objects.all()#.order_by('id')[::-1]

            context = {
                'message': 'could not found city.',
                'msg': 'alert alert-danger',
                'all_cities': all_cities

            }
            return render(request,'index.html',{'context':context})
        else:
            city_name=r['name']
            print(city_name)
            exisiting_city_cnt=City.objects.filter(name=city_name).count()
            print(exisiting_city_cnt)
            if exisiting_city_cnt < 1:
                city_weather={
                    'city':r['name'],
                    'temperature':r['main']['temp'],
                    'feels_like':r['main']['feels_like'],
                    'min_temp':r['main']['temp_min'],
                    'max_temp':r['main']['temp_max'],
                    'description':r['weather'][0]['description'],
                    'icon':r['weather'][0]['icon'],
                }
                print(city_weather)
                city=City()
                city.name=city_weather['city']
                city.temperature=city_weather['temperature']
                city.feels_like=city_weather['feels_like']
                city.min_temp=city_weather['min_temp']
                city.max_temp=city_weather['max_temp']
                city.description=city_weather['description']
                city.icon=city_weather['icon']
                city.save()
                all_cities=City.objects.all()#.order_by('id')[::-1]
                context={
                    'message':'successfully found city.',
                    'msg':'alert alert-success',
                    'all_cities':all_cities
                }
                return render(request,'index.html',{'context':context})
            else:
                all_cities = City.objects.all()#.order_by('id')[::-1]
                context={
                    'message':'city already exists.',
                    'msg':"alert alert-danger",
                    'all_cities':all_cities
                }
                return render(request,'index.html',{'context':context})
    all_cities = City.objects.all()#.order_by('id')[::-1]
    context = {
        'all_cities': all_cities
    }
    return render(request, 'index.html', {'context': context})


def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('index')