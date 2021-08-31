import requests, json, time

def updatePrices():
    url = 'https://prices.runescape.wiki/api/v1/osrs/latest'

    headers = {
        'User-Agent': 'High Alch Profit Finder', #user agent required for api access
    }

    responce = requests.get(url, headers=headers)

  
    with open('./prices.json', 'w') as f:
        json.dump(responce.text.replace('/', r'\/'), f, indent=4)
        f.close()

    seconds = time.time()

    with open("./time.txt", 'w') as f2:
        f2.write(str(seconds))
        f2.close()