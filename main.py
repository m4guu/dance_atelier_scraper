from flask import Flask, jsonify

from scraper import scrape_dance_atelier
from utils import make_soup

app = Flask(__name__)

# URL do scrapowania
URL = "https://danceatelier.pl/grafik/?doing_wp_cron=1713596003.2224550247192382812500"


@app.route('/scrape')
def scrape_and_return_json():
    soup = make_soup(URL)
    scrape_data = scrape_dance_atelier(soup)
    if scrape_data:
        # Zamień obiekty Day na słowniki przed serializacją do JSON-a
        days_as_dicts = [day.to_dict() for day in scrape_data]
        return jsonify(days_as_dicts)
    else:
        return jsonify({"error": "No data found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
