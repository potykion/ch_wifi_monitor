import datetime

import delorean


def dt_to_local(dt_str: str) -> datetime:
    """
    >>> dt_to_local("2019-05-12T12:42:28.767302Z").strftime("%Y-%m-%d %H:%M:%S")
    '2019-05-12 15:42:28'
    """
    parsed = delorean.parse(dt_str, dayfirst=False)
    return parsed.shift("Europe/Moscow").datetime


def to_mbs(bs: float) -> float:
    """
    >>> to_mbs(20396882.779735476)
    20.4
    """
    return round(bs / 10 ** 6, 2)
