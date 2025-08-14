# Weather App 🌤️

A beautiful and responsive Django-based weather application that provides real-time weather information for any city worldwide using the OpenWeatherMap API.

## Features

- 🌍 **Global Weather Data**: Get weather information for any city around the world
- 🎨 **Modern UI**: Clean, responsive design with glassmorphism effects
- 📱 **Mobile Friendly**: Fully responsive design that works on all devices
- 🌡️ **Comprehensive Data**: Display temperature, humidity, wind speed, and weather conditions
- ⚡ **Real-time Updates**: Fetch live weather data from OpenWeatherMap API
- 🔍 **Smart Search**: Easy city search with error handling
- 🎭 **Visual Icons**: Weather condition icons for better user experience


## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Icons**: Boxicons
- **API**: OpenWeatherMap API
- **Environment Management**: python-dotenv

## Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- Django 3.2 or higher
- An OpenWeatherMap API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd weather-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv weather_env
   source weather_env/bin/activate  # On Windows: weather_env\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install django requests python-dotenv
   ```

4. **Get OpenWeatherMap API Key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key

5. **Set up environment variables**
   - Create a `.env` file in your project root directory
   - Add your API key:
     ```
     api_key=your_openweathermap_api_key_here
     ```

6. **Configure Django settings**
   - Make sure your `settings.py` includes the weather app in `INSTALLED_APPS`
   - Configure static files settings

7. **Set up static files**
   - Create a `static` directory structure:
     ```
     static/
     ├── style.css
     └── images/
         ├── bg_image.jpg
         ├── 113.png
         └── 116.png
     ```

## Usage

1. **Start the Django development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your web browser
   - Navigate to `http://127.0.0.1:8000/`

3. **Using the weather app**
   - The app loads with Kolhapur as the default city
   - Enter any city name in the search box
   - Press the search button or hit Enter
   - View real-time weather information

## Project Structure

```
weather-app/
├── views.py              # Main application logic
├── templates/
│   └── index.html        # Main template file
├── static/
│   ├── style.css         # Custom styles (if any)
│   └── images/           # Background and icon images
├── .env                  # Environment variables (API key)
└── README.md            # This file
```

## API Integration

The app integrates with OpenWeatherMap API:
- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Parameters**: 
  - `q`: City name
  - `appid`: Your API key
  - `units`: metric (for Celsius)

## Key Features Explained

### Error Handling
- Displays user-friendly error messages for invalid cities
- Handles API failures gracefully
- Shows appropriate feedback for network issues

### Data Display
- **Temperature**: Current temperature in Celsius
- **Location**: City name and country code
- **Weather**: Main weather condition and description
- **Wind Speed**: Current wind speed in m/s
- **Humidity**: Current humidity percentage
- **Weather Icon**: Dynamic weather condition icon

### Responsive Design
- Mobile-first approach using Tailwind CSS
- Hover effects and smooth transitions
- Glassmorphism design elements
- Background image with overlay effects

## Customization

### Changing Default City
Edit the default city in `views.py`:
```python
city = request.GET.get('city', 'YourCityName')
```

### Adding More Weather Data
The OpenWeatherMap API provides additional data like:
- Feels like temperature
- Pressure
- Visibility
- UV index
- Sunrise/sunset times

### Styling
Customize the appearance by modifying:
- Background image in the body class
- Color scheme using Tailwind CSS classes
- Icon styles and animations

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your API key is correctly set in the `.env` file
   - Verify the API key is active (may take up to 10 minutes after creation)

2. **City Not Found**
   - Check the spelling of the city name
   - Try using the format "City, Country Code" (e.g., "London, UK")

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check your `STATIC_URL` and `STATICFILES_DIRS` settings

4. **Template Not Found**
   - Ensure the template is in the correct directory
   - Check your `TEMPLATES` setting in Django settings

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Boxicons](https://boxicons.com/) for the beautiful icons
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Create an issue in the repository
3. Contact the maintainers

---

**Note**: This is a demo application. For production use, implement proper error logging, rate limiting, and security measures.
