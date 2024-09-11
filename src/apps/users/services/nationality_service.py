import requests
import os
import json
from django.conf import settings

json_path = os.path.join(settings.BASE_DIR, 'apps/users/data/demonyms.json')

class NationalityService:
    @staticmethod
    def fetch_and_save_demonyms():
        if not os.path.exists(json_path):
            try:
                url = 'https://restcountries.com/v3.1/all'
                params = '?fields=name,demonyms'
                response = requests.get(url+params)
            except requests.exceptions.ConnectionError as e:
                print(f"Connection error: {e}, using coutnry names saved before instead.")
                return
            data = response.json()
            demonyms = {
                country["name"]["common"]: country["demonyms"]["eng"]["m"]
                for country in data
            }

            with open(json_path, 'w') as f:
                json.dump(demonyms, f)

    @staticmethod
    def load_demonyms():
        with open(json_path, 'r') as f:
            return json.load(f)
