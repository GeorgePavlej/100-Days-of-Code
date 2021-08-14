import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_keys = "f21d22c881f54aac3ce1f2e4b4e2e4ed"
account_sid = "AC7309b4fe59b3e287204ca6591078e715"
auth_token = "cb78debdf1a77db61e4df80a6609dc62"

parameters = {
    "lat": 18.693920,
    "lon": 83.623260,
    "appid": api_keys,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to be raining today. Remember to bring an umbrella.",
        from_='+18564223249',
        to='+4407897513276'
    )
    print(message.status)