import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 39.9075,
	"longitude": 116.3972,
	"daily": ["sunrise", "sunset"],
	"hourly": "temperature_2m",
}

response = requests.get(url, params=params)
data = response.json()
print(data)