import requests

city = input("Enter city: ")
url = f"http://wttr.in/{city}?format=3"   # wttr.in free weather API
response = requests.get(url)
print("Weather:", response.text)
