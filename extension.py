import requests
import json
from config import currency



class ConvertionExeption(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):


        if quote == base:
            raise ConvertionExeption(f'Две одинаковые валюты {base}')

        try:
            quote_sym = currency[quote]
        except KeyError:
            raise ConvertionExeption(f'Неизвестная валюта {quote}')

        try:
            base_sym = currency[base]
        except KeyError:
            raise ConvertionExeption(f'Неизвестная валюта {base}')

        try:
            amount = float(amount.replace(',','.'))
        except ValueError:
            raise ConvertionExeption(f'не правильно указано количество валюты {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_sym}&tsyms={base_sym}')
        total_base = json.loads(r.content)[currency[base]]*amount

        return total_base