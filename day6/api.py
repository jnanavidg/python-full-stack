# import requests

# url = "https://catfact.ninja/fact"
# reponse = requests.get(url)
# data = reponse.json()
# print(data)

import requests
api_key="0c962a94d697c20c6f88c7136f929819"
city=input("Enter the city name:")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
print("Status code:",response.status_code)
data=response.json()
print()
print("Weather info")
print("--------")
print("City:",data['name'])
print("Temperature:",data['main']['temp'])
print("Humidity:",data['main']['humidity'])