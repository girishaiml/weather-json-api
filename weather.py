import requests

API_KEY = "b0bc040f3eda49b7a97220712250506"  # replace with your key
city = "delray beach"
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
response = requests.get(url)
data = response.json()
temp = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
print(f"🌤️ Weather in {city}: {temp}°C, {condition}")
