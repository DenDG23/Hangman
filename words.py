from typing import Dict
import requests
r = requests.get('https://www.randomlists.com/data/words.json')
r = r.json()
words = r["data"]