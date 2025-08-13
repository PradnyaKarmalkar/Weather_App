from django.shortcuts import render
import requests 

def index(request):
    city = request.GET.get('city', 'Kolhapur')  # Default city
    api_key = '70da8fd98121c1a65a9159c7bfb51568'
    
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    api = requests.get(api_url).json()
    
    if api.get("cod") != 200:  # API returned an error
        error_message = api.get("message", "Error fetching data")
        return render(request, 'index.html', {"error": error_message})
    
    temperature = api['main']['temp']
    city = api['name']
    country = api['sys']['country']
    
    return render(request, 'index.html', {
        'temperature': temperature,
        'city': city,
        'country': country
    })
