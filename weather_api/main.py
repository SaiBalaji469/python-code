import requests
from twilio.rest import Client


account_sid = 'AC3983f35c7ad360dfa85c8c563a59c860'
auth_token = '93af3a6504d079d9899ad447b712691b'

api_key = "4ff04cc5a9994d6991292833231010"
API_END_POINT = "http://api.weatherapi.com/v1/current.json"

parameters = {
    "q": "Hyderabad",
    "key": api_key,
}

response = requests.get(API_END_POINT, params=parameters)
response.raise_for_status()
today_weather = response.json()["current"]["condition"]["text"]

if today_weather == "cloudy":
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+19518674837',
        to='+918919256799'
    )
print(message.status)

