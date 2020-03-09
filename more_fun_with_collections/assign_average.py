"""
Robert Walczak
The purpose of this program is to implement a switch/case with a dictionary.
:param key: key of value to be identified
:return: value of key or KeyError
"""


def switch_average(key):
    key_dict = {
        "A": 100,
        "B": 200,
        "C": 300,
        "D": 400,
        "E": 500
    }.get(key, KeyError)
    return key_dict