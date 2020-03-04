"""
Robert Walczak
A function to check if the value is in a set
:param this_dict: set of values or objects
:param a_value: value to check if in set
:return: True if value found or False if not
"""


def in_dict(this_dict, a_value):
    if a_value in this_dict:
        return True
    else:
        return False


if __name__ == '__main__':
    in_dict()