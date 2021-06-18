"""
    Regex stuff
    ===========

    To experiment with regex: https://regex101.com/
    Documentation: https://docs.python.org/3/howto/regex.html


"""

import re

regex = re.compile(r"(\d{1,5}(h|s|m|d))")
times = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600*24}


def convert_time(time: str) -> int:
    """
        >>> convert_time('10s')
        10
        >>> convert_time('2m')
        120
        >>> convert_time('2m 10s')
        130
        >>> convert_time('1d 3h 2m 10s')
        97330

        :return:
    """

    endresult = 0
    data = re.findall(regex, time)

    for key in data:
        value = int(key[0][:-1])
        result = value * times[key[1]]
        endresult += int(result)

    return endresult


if __name__ == '__main__':
    convert_time('10d')
