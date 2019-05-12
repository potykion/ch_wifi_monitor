from dateutil.parser import parse


def format_date(timestamp_str: str) -> str:
    """
    >>> format_date("2019-05-12T12:42:28.767302Z")
    '2019-05-12 12:42:28'
    """
    return parse(timestamp_str).strftime("%Y-%m-%d %H:%M:%S")


def to_mbs(bs: float) -> float:
    """
    >>> to_mbs(20396882.779735476)
    20.4
    """
    return round(bs / 10 ** 6, 2)
