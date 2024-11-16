import requests

def get_weather_conditions(city):
    api_key = "7b2924743ca4eb6a5d72b1e0e8b87804"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make an API request to OpenWeatherMap
        response = requests.get(url)
        data = response.json()
        
        # Check if the response contains valid data
        if data["cod"] == 200:
            # Extract temperature and weather description
            temperature = data["main"]["temp"]
            conditions = data["weather"][0]["description"]
            
            # Display the weather information
            print(f"The current temperature in {city} is {temperature}°C.")
            print(f"The weather conditions are {conditions}.")
            
            # Check if it’s going to rain or be sunny
            if "rain" in conditions:
                print("It looks like it’s going to rain.")
            elif "clear" in conditions:
                print("The weather is sunny.")
            else:
                print("The weather is likely cloudy or mixed.")
        else:
            print("City not found. Please enter a valid city name.")
    
    except Exception as e:
        print("An error occurred:", e)

# Get user input for city name
city = input("Enter the city name to check the weather: ")
get_weather_conditions(city)
