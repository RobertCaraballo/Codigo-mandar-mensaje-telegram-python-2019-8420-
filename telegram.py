#matricula: 2019-8420

import requests
import json
from urllib.request import urlopen

r = requests.post('https://api.telegram.org/bot<TAKEN>/sendMessage',
                  data={'chat_id': '<CHAT ID>', 'text': '<TEXT>'})
data = json.loads(r.text)
print(data)

