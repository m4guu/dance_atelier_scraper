import json
import time
from datetime import datetime

from scraper import scrape_dance_atelier
from utils import make_soup


def scrape_and_save():
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    url = "https://danceatelier.pl/grafik/?doing_wp_cron=1713596003.2224550247192382812500"
    soup = make_soup(url)

    scrape_data = scrape_dance_atelier(soup)

    with open(f"data/{current_datetime}.json", "w") as json_file:
        json.dump([day.__dict__ for day in scrape_data], json_file,
                  indent=4, default=lambda x: x.__dict__)


while True:
    scrape_and_save()
    time.sleep(10)
