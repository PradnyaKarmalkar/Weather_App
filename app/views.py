from django.shortcuts import render
import requests 

def index(request):
    city = request.GET.get('city', 'Kolhapur')  # Default city
    api_key = '70da8fd98121c1a65a9159c7bfb51568'
    
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    print(api_url)  # Debugging line to check the API URL
    
    api = requests.get(api_url).json()
    
    if api.get("cod") != 200:  # API returned an error
        error_message = api.get("message", "Error fetching data")
        return render(request, 'index.html', {"error": error_message})
    
    temperature = api['main']['temp']
    city = api['name']
    country = api['sys']['country']
    wind_speed = api['wind']['speed']
    humidity = api['main']['humidity']
    
    icon_url =' https://openweathermap.org/img/wn/10d@2x.png'
    print(icon_url)
    icon_id=api['weather'][0]['icon']
    weather=api['weather'][0]['main']
    description=api['weather'][0]['description']
    
    
    
    return render(request, 'index.html', {
        'temperature': temperature,
        'city': city,
        'country': country,
        'wind_speed': wind_speed,
        'humidity': humidity,
        'weather': weather,
        'description': description,
        'icon_url': icon_url,
        
    })
