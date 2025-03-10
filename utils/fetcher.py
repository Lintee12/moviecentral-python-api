import requests
from bs4 import BeautifulSoup

class Fetcher:
    # returns bs4 object
    @staticmethod
    def fetch(url: str):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except Exception as e:
            raise Exception(f"Error Fetching: {e}")

class SourceFetcher:
    # returns json sources object
    @staticmethod
    def fetch(url: str):
        try:
            response = requests.get(url)
            sources = response.json()
            return sources
        except Exception as e:
            raise Exception(f"Error Fetching: {e}")