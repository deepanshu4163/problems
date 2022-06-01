import requests
import os

api_key = os.environ.get('WEATHER_API_KEY')    #hiding api_key using environ variable
city = input("enter name of the city: ")        #taking input from the user

#calling weather api using get method, passing city and api_key as query parameters
#.json() method converts json response into python dictionary
weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').json()
response = weather_response

#storing data into variable and converting kelvin into celcius
temp = response['main']['temp'] - 273
temp_min = response['main']['temp_min'] - 273
temp_max = response['main']['temp_max'] - 273
feels_like = response['main']['feels_like'] - 273
humidity = response['main']['humidity'] 
wind_speed = response['wind']['speed'] 
description = response['weather'][0]['description']
city_name = response['name']

#printing data
print("temperature: " + "{:.2f} deg celcius".format(temp))
print("min temp: " + "{:.2f} deg celcius".format(temp_min))
print("max temp: " + "{:.2f} deg celcius".format(temp_max))
print("feels like: " + "{:.2f} deg celcius".format(feels_like))
print("humidity: " + str(humidity))
print("wind speed: " + str(wind_speed))
print("description: " + str(description))
print("city name: " + str(city_name))