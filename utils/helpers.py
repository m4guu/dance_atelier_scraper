import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during request to {url}: {e}")
        # TODO: add error handling
        return None


def make_soup(web_url):
    html_content = get_html(web_url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    # TODO: add error handling
    print(f"Error during making soup.")
    return None
