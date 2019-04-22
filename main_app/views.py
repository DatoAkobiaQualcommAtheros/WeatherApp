
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=54410fad62887f6460fa74a2a427d627'
    if request.method == 'POST':
        form = CityForm(request.POST)



    form = CityForm()
    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : int(r['main']['temp']) - 273,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
    context = {'weather_data': weather_data, 'form':form}
    return render(request, 'main_app/index.html', context)
