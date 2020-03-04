"""
Robert Walczak
The purpose of this program is to return a True if a value is found in a set or a False if it is not.
:param this_set: set of numbers
:param a_value: value to check if in set
:return: True if value found or False if not
this would be handy for data analysis
"""
def in_set(this_set, a_value):
    if a_value in this_set:
        return True
    else:
        return False


if __name__ == '__main__':
    in_set()