#!/usr/bin/python3
import requests 
import json
import time
crypto_url = "https://api.cryptonator.com/api/ticker/eth-eur"
#cryptos = ["btc", "eth"]

headers = {
	'User-Agent': 'My User Agent 1.0'
}
def cryptokurs():
	kurs = float(json.loads(requests.request("GET", crypto_url, headers=headers).text)["ticker"]["price"])
	return kurs
kurs = cryptokurs()
f = open("crypto", "w")
f.write("kurs = " + str(kurs))
f.close()
#file.write(kurs)
while True:
	kurs = cryptokurs()
	print(kurs)
	time.sleep(10)
