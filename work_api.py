import requests
import json


def intr_numbers():
    with open('dataset_24476_3.txt') as f, open('otv.txt', 'w') as o:
        for chislo in f.readlines():
            response = requests.get(f'http://numbersapi.com/{chislo.strip()}/math?json==true')
            data = json.loads(response.text)  # json dict
            if data['found']:
                print('Interesting', file=o)
            else:
                print('Boring', file=o)


def artists():
    client_id = 'ec271b546f7a0ee89816'
    client_secret = '28b273f3dd63d978dadd5c144aa090b1'

    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    token = j["token"]
    headers = {"X-Xapp-Token": token}
    with open('dataset_24476_4.txt', encoding='utf-8') as inp, open('otp.txt', 'w', encoding='utf-8') as otp:
        dic = {}
        for iden in inp.readlines():
            r = requests.get(f"https://api.artsy.net/api/artists/{iden.strip()}", headers=headers)
            j = json.loads(r.text)
            dic[j['birthday']] = j['sortable_name']
        ls = sorted(dic.items(), key=lambda x: (x[0], x[1]))
        [print(i[-1], sep='\n', file=otp) for i in ls]
