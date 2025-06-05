import requests

API_KEY = "b0bc040f3eda49b7a97220712250506"  # ← replace with your real key
city = "delray beach"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

# Make the API request
response = requests.get(url)

# Convert JSON response to Python dict
data = response.json()

# Extract useful info
temp = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]

# Print result
print(f"🌤️ Weather in {city}: {temp}°C, {condition}")
