import json
import requests


city_name = "Saint Petersburg"
api_key = "ae5632602334b079d5c2b4e90057b430"

def get_weather(city_name, api_key):
    # Define the API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Make the request to the API
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extract relevant data
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            
            # Print the weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} hPa")
            print(f"Description: {description.capitalize()}")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
            print(data.get('message', 'Unknown error'))
    
    except Exception as e:
        print(f"An error occurred: {e}")


api_key = 'ae5632602334b079d5c2b4e90057b430'
city_name = 'Saint Petersburg'  

get_weather(city_name, api_key)


import requests
import json

def get_news(api_key, country='us', category=None, sources=None):
    # Define the API endpoint
    url = "https://newsapi.org/v2/top-headlines"
    
    # Define parameters for the request
    params = {
        'apiKey': api_key,
        'country': country,  # Specify the country (e.g., 'us' for United States)
        'category': category,  # Optional: Specify a category (e.g., 'business', 'technology')
        'sources': sources,  # Optional: Specify sources (e.g., 'bbc-news')
    }
    
    try:
        # Make the request to the API
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            # Extract articles from the response
            articles = data['articles']
            
            # Print structured output for each article
            for i, article in enumerate(articles[:5]):  # Show top 5 articles
                print(f"Article {i + 1}:")
                print(f"Title: {article['title']}")
                print(f"Author: {article['author'] or 'N/A'}")
                print(f"Source: {article['source']['name']}")
                print(f"Description: {article['description']}")
                print(f"URL: {article['url']}")
                print(f"Published At: {article['publishedAt']}\n")
        else:
            print(f"Error: Unable to fetch news data. Status code: {response.status_code}")
            print(data.get('message', 'Unknown error'))
    
    except Exception as e:
        print(f"An error occurred: {e}")

api_key = 'e53dd6c3e004483e9a2460ad9c8b3d3a'

# Fetch top headlines for the US
get_news(api_key, country='us', category='general')