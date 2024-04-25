from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import StockData
from django.conf import settings
from .serializers import StockDataSerializer
from rest_framework import views, status
from rest_framework.response import Response
import requests

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


@api_view(['GET','POST'])
def stock_list(request):
    if request.method == 'GET':
        stock = StockData.objects.all()
        serializer = StockDataSerializer(stock, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)