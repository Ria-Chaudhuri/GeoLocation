import pandas as pd
import requests
import time
import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

BASE_URL = 'https://api.ipgeolocation.io/ipgeo'
API_KEY = os.getenv('IP_GEOLOCATION_API_KEY')

def geocode_ip(ip_address):
    """
        Geocode a single IP address.

        :param ip_address: The IP address to geocode.
        :return: Geocoded data as a dictionary or None if an error occurs.
       """
    try:
        response = requests.get(BASE_URL, params={'apiKey': API_KEY, 'ip': ip_address}, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None


def batch_ips_processing(ip_addresses, batch_size=100,delay=1):
    """
        Process a list of IP addresses in batches.

        :param ip_addresses: List of IP addresses to process.
        :param batch_size: Number of IPs to process in each batch.
        :param delay: Delay between requests to avoid hitting rate limits.
        :return: List of geocoded results.
    """
    results=[]
    for i in range(0, len(ip_addresses), batch_size):
        batch = ip_addresses[i:i + batch_size]
        for ip in batch:
            result= geocode_ip(ip)
            if result:
                results.append(result)
            time.sleep(delay)  # Small delay to avoid hitting rate limits
    return results
