import pandas as pd
import json
import requests
import time
import os
from pathlib import Path
import logging

from geocode_function import geocode_ip, batch_ips_processing

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Load IP addresses from the CSV file
        input_file = Path('data/ip_addresses.csv')
        if not input_file.is_file():
            logging.error(f"Input file {input_file} does not exist.")
            return
        
        # Load IP address from the CSV file
        ip_df=pd.read_csv('data/ip_addresses.csv')
        ip_addresses = ip_df['ip_address'].tolist()


        #Process the IPs from the CSV file
        geocoded_ips=batch_ips_processing(ip_addresses)


        # Save the results to a JSON file
        output_file = Path('data/geocoded_ips.json')
        with open(output_file, mode='w') as file:
            json.dump(geocoded_ips, file, indent=4)  # Save the list of dictionaries to a JSON file
        logging.info(f"Geocoded data successfully saved to {output_file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

