import requests
import json

with open('dataset_24476_3.txt') as f, open('otv.txt','w') as o:
    for chislo in f.readlines():
        response = requests.get(f'http://numbersapi.com/{chislo.strip()}/math?json==true')
        data = json.loads(response.text)  # json dict
        if data['found'] == True:
            print('Interesting',file=o)
        else:
            print('Boring',file=o)

