# trevolt
Codigo api

import requests
import json
from urllib.request import urlopen

r = requests.post('https://api.telegram.org/bot1067307006:AAEna_k0hMSR1phREGMuYJ8JfRQHFOIc92w/sendMessage',
                  data={'chat_id': '<CHAT ID>', 'text': '<TEXT>'})
data = json.loads(r.text)
print(data['ok'])
