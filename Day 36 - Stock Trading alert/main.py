import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api_key = "556d06aa9fc54f30a330cc7c7f1dc082"
stock_api_keys = "BBKRI7S8EM6OBCYH"

account_sid = "AC7309b4fe59b3e287204ca6591078e715"
auth_token = "1831b085e524b7392b2be05ade0ca500"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_keys,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

price_difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if price_difference > 0:
    up_down = "☝️"
else:
    up_down = "👇"

percentage_difference = (price_difference / yesterday_closing_price) * 100
if abs(percentage_difference) > 0.21:
    news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
response_news.raise_for_status()
articles = response_news.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles
first_three_articles = articles[:3]

#Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article = [f"Headline: {article['title']}, \n'Brief': {article['description']}" for article in first_three_articles]

#Send each article as a separate message via Twilio.

for article in formatted_article:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{STOCK_NAME}: {percentage_difference:.2f}% {up_down} \n {article}",
        from_='+18564223249',
        to='+447897513276',
)
