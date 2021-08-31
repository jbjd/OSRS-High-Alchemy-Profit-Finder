# OSRS-High-Alchemy-Profit-Finder
Gets data from runescape.wiki's API to find and list most profitable items to cast high alchemy on in the game of Runescape.

Notes to run: As stated on https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices  It is preferable to leave some contact information, such as a discord, in the header. To do so, you can add yours in the file 'get_prices.py' at the end of the string 'High Alch Profit Finder'.
Example: 'High Alch Profit Finder - yourNameHere#1234'

The program is also set to only update prices every 480 seconds to not send too many requests to the API. If you would like prices to update faster, change the variable UPDATE_TIME at the top of price_compare.py.


