#Will be using api keys from www.openweathermap.org

import requests

apiKey = '8e7c892a9ab45df1e77d686c1b963a4b'
userInput = input("Enter City: ")
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={apiKey}")

if weatherData.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weatherData.json()['weather'][0]['main']
    temp = round(weatherData.json()['main']['temp'])

    print(f"The weather in {userInput} is: {weather}")
    print(f"The temperature in {userInput} is: {temp}°F")


