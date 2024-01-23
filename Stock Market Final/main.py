import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "50L3932JORJGCAXU"
NEWS_API_KEY = "5ea8f78bfa5b46aea397d63c02b7f1c2"

TWILIO_SID = "AC3a46f947c5f51844d6af50cce573c875"
TWILIO_AUTH = "da2c1b0aac61d1faf9ff56b8d506499c"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,


}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_per = (difference / float(yesterday_closing_price)) * 100
print(diff_per)

if diff_per > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }


    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]


    formatted_list = [f"Headline: {article['title']}.\nBreif:{article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH)

    for article in formatted_list:
        message = client.messages.create(
            body= article,
            from_='+12053410790',
            to='+918919256799'
        )





