import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def parse_weather_data(self, data):
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        return {
            'temperature': main.get('temp'),
            'humidity': main.get('humidity'),
            'description': weather.get('description'),
            'city': data.get('name')
        }

def main():
    # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
    api_key = "your_api_key_here"
    weather_service = WeatherService(api_key)

    city = input("Enter the city name: ")
    try:
        weather_data = weather_service.get_weather(city)
        parsed_data = weather_service.parse_weather_data(weather_data)
        print(f"Weather in {parsed_data['city']}:")
        print(f"Temperature: {parsed_data['temperature']}°C")
        print(f"Humidity: {parsed_data['humidity']}%")
        print(f"Description: {parsed_data['description']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    main()