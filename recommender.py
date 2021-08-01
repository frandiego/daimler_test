import json
from itertools import chain, combinations
from math import factorial

import numpy as np


class SkuRecommender:
    file_path: str = './data/Daimler-test-data.json'
    main: dict = None
    main_key: str = None
    main_values: np.array = None
    stock: dict = None

    @staticmethod
    def tidy(sku):
        
        return np.array(list(map(lambda i: int(i.split('-')[-1]), sku.values())))

    def view(self, key: str):
        values = list(self.stock.get(key))
        if values:
            return {key: dict(map(lambda i, j: (f'att-{i}', f'att-{i}-{j}'), 'abcdefghij', values))}

    def read_stock(self):
        if not self.stock:
            output = {}
            with open(self.file_path, 'r') as file:
                json_file = json.load(file)
                for key, value in json_file.items():
                    if len(value) != 10:
                        raise ValueError(f"SKU {key} is not well formated, should have 10 elements")
                    output[key] = self.tidy(value)
            self.stock = output

    def keys(self):
        self.read_stock()
        return list(self.stock.keys())

    def set_main(self, sku: str):
        self.read_stock()
        self.main_key = sku
        self.main_values = self.stock.get(self.main_key)
        self.main = {self.main_key: self.main_values}
        self.stock_same_items = self.get_stock_by_same_items_with_main()

    def get_stock_by_same_items_with_main(self):
        filter_stock = filter(lambda i: i[0] != self.main_key, self.stock.items())
        same_values = map(lambda i: (i[0], sum(self.main_values == i[1])), dict(filter_stock).items())
        return dict(filter(lambda i: i[1] > 0, same_values))

    def is_same_index(self, sku_values: np.array, idx: list):
        return all(np.take(self.main_values, idx) == np.take(sku_values, idx))

    def stock_same_index(self, stock: dict, idx: list):
        return dict(filter(lambda i: self.is_same_index(i[1], idx), stock.items()))

    def make_combination(self, n: int):
        l = range(n)
        combinations_lenght = sorted(range(1, len(l) + 1), reverse=1)
        return chain(*map(lambda i: combinations(l, i), combinations_lenght))

    def filter_keys(self, stock: dict, filter_keys: list = []):
        return {k: v for k, v in stock.items() if k not in filter_keys}

    def stock_filter_same_lenght(self, n: int):
        return dict(filter(lambda i: len(i[1]) == n, self.stock_same_items.items()))

    def stock_filter(self, n: int, filter_keys: list = []):
        return {k: v for k, v in self.stock_filter_same_lenght(n).items() if k not in filter_keys}

    def max_same(self):
        return max(map(lambda i: sum(self.main_values == i), self.stock.values()))

    def make_recommendations(self, top: int = 10):
        recommendations = []
        for n in sorted(set(self.stock_same_items.values()), reverse=1):
            stock = {k: self.stock.get(k) for k, v in self.stock_same_items.items() if v == n}
            c = 0
            n_comb = factorial(10) / (factorial(n) * factorial(10 - n))
            for comb in combinations(range(10), n):
                c += 1
                rec_keys = list(self.stock_same_index(stock, comb).keys())
                rec_keys = [(i, n + (n_comb - c) / n_comb) for i in rec_keys]
                recommendations.extend(rec_keys)
                if len(recommendations) >= top:
                    return recommendations
