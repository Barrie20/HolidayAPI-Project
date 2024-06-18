import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def get_holidays(country, year):
    api_key = os.getenv('API_KEY')
    base_url = "https://holidayapi.com/v1/holidays"

    params = {
        'key': api_key,
        'country': country,
        'year': datetime.now().year-1
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()['holidays']  # Return inside the function
    else:
        return None

if __name__ == "__main__":
    country_code = "SL"  # Example: India
    year = datetime.now().year-1

    holidays = get_holidays(country_code, year)

    if holidays:
        for holiday in holidays:
            print(f"{holiday['date']}: {holiday['name']}")
    else:
        print("Error fetching holiday data.")
