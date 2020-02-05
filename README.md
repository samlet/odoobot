# odoobot
## step 1
```bash
$ rasa train
$ rasa run actions
$ rasa run
```

# step 2
```python
import requests
from pprint import pprint

port=5005
text = f'/act_products'
data = {'sender': 'default', "message": text}
response = requests.post(f'http://localhost:{port}/webhooks/rest/webhook', json=data)
# print('status code:', response.status_code)
if response.status_code==200:
    pprint(response.json())
```

