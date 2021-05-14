import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

URL = 'https://myfin.by/currency/usd'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': '*/*'}


def parse():
    html = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find_all('tr', class_='tr-tb')

    banks = []
    for item in items:
        banks.append(
            {
                'name_bank': item.find('span', class_='iconb').get_text(),
                'buy': float(item.find_all('td')[1].get_text()),
                'sell': float(item.find_all('td')[2].get_text())
            }
        )

    max_buy = banks[0]['buy']
    min_sell = banks[0]['sell']

    for bank in banks:

        if bank['buy'] > max_buy:
            max_buy = bank['buy']

        if bank['sell'] < min_sell:
            min_sell = bank['sell']

    def max_currency_buy():
        list_banks = []
        for bank_ in banks:
            if bank_['buy'] == max_buy:
                list_banks.append(bank_['name_bank'])

        return list_banks

    def min_currency_sell():
        list_banks = []
        for bank_ in banks:
            if bank_['sell'] == min_sell:
                list_banks += [bank_['name_bank']]

        return list_banks

    messages_ = list()
    max_currency_buy = max_currency_buy()
    min_currency_sell = min_currency_sell()
    messages_.append('Максимальный курс покупки: {}. {}'.format(max_buy,
                     'Предлагает банк: ' if len(max_currency_buy) == 1 else 'Предлагают банки: '))

    messages_.append(', '.join(max_currency_buy))
    messages_.append('Минимальный курс продажи: {}. {}'.format(min_sell,
                     'Предлагает банк: ' if len(min_currency_sell) == 1 else 'Предлагают банки: '))
    messages_.append(', '.join(min_currency_sell))

    return messages_



