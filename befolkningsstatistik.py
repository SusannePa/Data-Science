which -a pythonwhich

import requests

def get_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

url = 'https://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101G/BefforandrKvRLK'
data = get_data_from_url(url)
if data:
    print(data)
else:
    print("Failed to retrieve data")