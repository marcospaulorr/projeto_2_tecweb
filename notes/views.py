from django.shortcuts import render
import requests
from .models import StockData
from django.conf import settings

def fetch_and_store_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    for date, stats in data['Time Series (Daily)'].items():
        StockData.objects.create(
            date=date,
            open=stats['1. open'],
            high=stats['2. high'],
            low=stats['3. low'],
            close=stats['4. close'],
            volume=stats['5. volume']
        )

