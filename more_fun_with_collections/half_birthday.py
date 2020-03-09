"""Robert Walczak
The purpose of this program is to find your half birthday.
:param b_day: most recent birthday
:return: half birthday
"""

from datetime import date, timedelta


def half_birthday(b_day):
    # 365/2 = 182.5
    half_b_day = b_day + timedelta(days=182.5)
    return half_b_day
