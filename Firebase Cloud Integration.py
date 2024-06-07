import requests

class SmartIrrigationSystem:
    def __init__(self):
        self.weather_api_key = 'facc375186f6a37afb6d1ac1e32d88db'
        self.crop_parameters = {
            'nitrogen': 0,
            'phosphorus': 0,
            'potassium': 0,
            'temperature': 0,
            'humidity': 0,
            'ph': 0
        }

    def get_real_time_weather(self, city):
        # Replace 'your_weather_api_key' with your actual API key
        weather_api_url = f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={self.weather_api_key}'

        try:
            response = requests.get(weather_api_url)
            data = response.json()

            if 'main' in data and 'temp' in data['main'] and 'humidity' in data['main']:
                return data
            else:
                print("Invalid response format. Unable to fetch weather data.")
                return None
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None

    def adjust_schedules_based_on_weather(self, city):
        weather_data = self.get_real_time_weather(city)

        if weather_data:
            # Extract relevant weather parameters
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            # Update crop parameters
            self.crop_parameters['temperature'] = temperature
            self.crop_parameters['humidity'] = humidity

            # Adjust irrigation and fertilizer schedules based on weather conditions
            if temperature > 30:
                self.crop_parameters['nitrogen'] += 10
            elif temperature < 20:
                self.crop_parameters['nitrogen'] -= 10

            if humidity > 80:
                self.crop_parameters['phosphorus'] += 5
            elif humidity < 60:
                self.crop_parameters['phosphorus'] -= 5

            print("Adjusted schedules based on weather conditions:")
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
            print("Updated crop parameters:", self.crop_parameters)
        else:
            print("Unable to fetch weather data. Schedules remain unchanged.")

# Example usage
if __name__ == "__main__":
    irrigation_system = SmartIrrigationSystem()
    city_name = "YourCity,YourCountry"  # Replace with the actual city and country

    irrigation_system.adjust_schedules_based_on_weather(city_name)
