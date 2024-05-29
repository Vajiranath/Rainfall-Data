import os
import json
import requests
import zipfile
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s',
                    handlers=[
                        logging.FileHandler("data_update.log"),
                        logging.StreamHandler()
                    ])

SOUTH_URL = "https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=SOUTH&zip=1"
NORTH_URL = "https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=NORTH&zip=1"
DATA_FILE = 'data/rainfall_data.json'
METADATA_FILE = 'data/rainfall_metadata.json'


def download_and_extract(url, extract_to='data'):
    logging.info(f"Downloading data from {url}")
    response = requests.get(url)
    zip_path = os.path.join(extract_to, 'temp.zip')
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    logging.info(f"Extracting data to {extract_to}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    os.remove(zip_path)
    json_files = [f for f in os.listdir(extract_to) if f.endswith('.json')]
    if json_files:
        with open(os.path.join(extract_to, json_files[0]), 'r') as file:
            data = json.load(file)
        os.remove(os.path.join(extract_to, json_files[0]))
        return data
    return None


def load_existing_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"data": {"item": []}}


def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as file:
            return json.load(file)
    return {"data": {"item": []}}


def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def check_and_update_data():
    today = datetime.now().strftime('%Y-%m-%d')
    logging.info(f"Checking and updating data for {today}...")
    south_data = download_and_extract(SOUTH_URL)
    north_data = download_and_extract(NORTH_URL)
    
    if not south_data or not north_data:
        logging.error("Failed to download data")
        return

    new_data = south_data['data']['item'] + north_data['data']['item']
    logging.info(f"Downloaded {len(new_data)} items.")

    existing_data = load_existing_data()
    existing_sites = {item['SITE_NO']: item for item in existing_data['data']['item']}
    updated = False
    new_items_count = 0
    updated_items_count = 0

    for item in new_data:
        site_no = item['SITE_NO']
        if site_no in existing_sites:
            if existing_sites[site_no] != item:
                logging.info(f"Updating data for site {site_no}")
                existing_sites[site_no] = item
                updated = True
                updated_items_count += 1
        else:
            logging.info(f"Adding new site {site_no}")
            existing_sites[site_no] = item
            updated = True
            new_items_count += 1

    if updated:
        save_data({"data": {"item": list(existing_sites.values())}})
        logging.info(f"Data updated successfully with {new_items_count} new items and {updated_items_count} updated items.")
    else:
        logging.info("No updates found")


def scheduled_task():
    check_and_update_data()
