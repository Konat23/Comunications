# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 00:44:46 2022

@author: juans


# Author: Sebastian Garcia

raw_data = {' ': 7,
            'a': 4,
            'e': 4,
            'f': 3,
            'h': 2,
            'i': 2,
            'm': 2,
            'n': 2,
            's': 2,
            't': 2,
            'l': 1,
            'o': 1,
            'p': 1,
            'r': 1,
            'u': 1,
            'x': 1}"""

raw_data = {'a': 8,
            'b': 8,
            'c': 4,
            'd': 4,
            'e': 2,
            'f': 2}

class Value():
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
        self.code = float('nan')

    def get_value(self):
        return self.value

    def __str__(self):
        return '{}: {}'.format(self.symbol, self.code)

    def set_code(self, code):
        self.code = code


class Node():
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def get_value(self):
        return self.value1.get_value() + self.value2.get_value()

    def __str__(self):
        return '[{} {} {}]'.format(self.value1, self.get_value(), self.value2)

    def set_code(self, code):
        self.value1.set_code(code+'0')
        self.value2.set_code(code+'1')


def convert_data(data):
    converted = []
    for symbol in data:
        converted.append(Value(symbol, data[symbol]))
    return converted


def Huffman(data):
    data = data.copy()
    # Sort
    def get_sort_key(obj):
        return obj.get_value()


    while len(data) > 1:
        data.sort(key=get_sort_key, reverse=False)

        # Huffman Tree
        new_node = Node(data[1], data[0])
        del data[0]
        del data[0]
        data.insert(0,new_node)

    data[0].set_code('')
    return data[0]


def print_dict(data):
    for symbol in data:
        print(symbol)


if __name__ == '__main__':
    data = convert_data(raw_data)
    tree = Huffman(data)
    print(tree)
    print()
    print('----------------------------')
    print()
    print_dict(data)
