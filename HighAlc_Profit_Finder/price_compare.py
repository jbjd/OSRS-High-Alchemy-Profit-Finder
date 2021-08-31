import get_prices
from alchItem import alchItem
import json, time

if __name__ == "__main__":

    with open('./time.txt', 'r') as timeReader: #get time of last api call
        curTime = timeReader.read().split(".")[0]

    seconds = int(time.time())#current time

    if(seconds > int(curTime)+480 ):#if 480 seconds passed, call api again. Otherwise, use older data to not stress server / faster results
        print("Fetching Updated Prices...\n")
        get_prices.updatePrices()

    with open('./prices.json', 'r') as file:#get prices
        f = file.read().replace('\n', '')

    data = json.loads(f)
    data2 = json.loads(data)#load it twice for some reason; loading once only ended up a string, but two loads works like a charm
    #dictionary with item's id and list with item's name, buy limit, and high alch value
    idFinder = {'2501' : ["Red D'hide body", 70, 6738], '2499' : ["Blue D'hide body", 125, 5616], '1149' : ['Dragon med helm',8,60000], '3054':['Mystic lava staff',8,27000], '1135' : ["Green D'hide body", 125, 4680]}
    dataStrings = list()
    print('{:18} | {:6} | {:9} '.format('Name','Profit','Buy Limit'))
    for k in idFinder.keys():
        itemData = idFinder[k]
        profit = itemData[2]-data2['data'][k]['high']
        dataString = '{:18} | {:>6} | {:9} '.format(itemData[0],profit,itemData[1])
        dataStrings.append(alchItem(dataString,profit))
    dataStrings.sort(key=lambda item : item.val, reverse=True)#sort by profit
    for st in dataStrings:
        print(st)