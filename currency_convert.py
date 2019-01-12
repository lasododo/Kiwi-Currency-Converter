import argparse
import urllib.request
import os
import json
import ast

from termcolor import colored
from bs4 import BeautifulSoup
from itertools import islice

JSON_OF_ALL_CURRENCIES = """http://data.fixer.io/api/latest?access_key=d281dc374b673b7c0976a6feeb27c2ca&format=1"""
SHORTCUT_TO_SYMBOL = """https://gist.githubusercontent.com/Fluidbyte/2973986/raw/b0d1722b04b0a737aade2ce6e055263625a0b435/Common-Currency.json"""


class ErrorHandler(Exception):
    pass


class FileUpdate:
    def __init__(self, filename, json_txt):
        fp = urllib.request.urlopen(json_txt)
        my_bytes = fp.read()
        fp.close()
        json_txt = BeautifulSoup(my_bytes, "lxml").get_text()
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'w') as f:
            f.write(json_txt)


class CurrencyConvert:
    def __init__(self, amount, input_currency, output_currency=None):
        self.amount_default = amount
        self.amount = amount
        self.input_currency = self.update_symbols(input_currency)
        self.output_currency = self.update_symbols(output_currency)
        self.amount = self.convert_input()
        if output_currency is None:
            self.result = self.convert_all()
        else:
            self.result = self.convert_it()

    @classmethod
    def update_symbols(cls, symbol):
        json_search = '"symbol": "{}"'.format(symbol)
        with open('backup/symbols.json', 'r') as f:
            getter = False
            for line in f:
                if getter:
                    data = ast.literal_eval('{' + line + '}')
                    return data['code']
                elif json_search in line:
                    getter = True
                    next(islice(f, 4, 4), None)
        return symbol

    def convert_it(self):
        with open("backup/currency.json") as json_file:
            data = json.load(json_file)
            for key, value in data['rates'].items():
                if key == self.output_currency:
                    return {key: self.amount * value}
        raise Exception('Error during converting')

    def convert_input(self):
        with open("backup/currency.json") as json_file:
            data = json.load(json_file)
            for key, value in data['rates'].items():
                if key == self.input_currency:
                    return self.amount_default / value
        raise Exception('Wrong currency')

    def convert_all(self):
        json_output = {}
        with open("backup/currency.json") as json_file:
            data = json.load(json_file)
            for key, value in data['rates'].items():
                json_output[key] = self.amount * value
        return json_output

    def json_it(self):
        input_part = {"amount": self.amount_default, "currency": str(self.input_currency)}
        output_part = self.result
        return {"input": input_part, "output": output_part}


def update_files():
    try:
        FileUpdate("backup/symbols.json", SHORTCUT_TO_SYMBOL)
        FileUpdate("backup/currency.json", JSON_OF_ALL_CURRENCIES)
    except ErrorHandler:
        print(colored('WE COULD NOT UPDATE THE DATA, THE CURRENCY CONVERTER CAN BE NOT ACCURED', 'red'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--amount",
                        type=float,
                        help="Amount you want to convert",
                        required=True)
    parser.add_argument("--input_currency",
                        type=str,
                        help="input currency -> 3 letters / symbol",
                        required=True)
    parser.add_argument("--output_currency",
                        type=str,
                        help="output currency -> 3 letters / symbol")

    args = parser.parse_args()
    update_files()

    if args.output_currency is not None:
        args.output_currency = args.output_currency.upper()

    currency = CurrencyConvert(args.amount, args.input_currency.upper(), args.output_currency)
    json_text = currency.json_it()
    print(json.dumps(json_text, indent=10))
