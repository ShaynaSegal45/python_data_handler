import requests
import logging
import time
from typing import List, Dict
from requests.exceptions import RequestException

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_candidate_data(url: str, retries: int = 3) -> List[Dict]:
    for _ in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                logging.info("Successfully fetched data.")
                return response.json()
            else:
                logging.error(f"Failed to fetch data. Status Code: {response.status_code}")
        except RequestException as e:
            logging.error(f"Error fetching data: {e}")
            time.sleep(5)  
    return []
