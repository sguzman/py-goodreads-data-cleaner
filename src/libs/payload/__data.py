import csv
import functools
import logging
from typing import List
from typing import Tuple


__csv_path: str = './.env/data/goodreads.csv'


@functools.cache
def exec() -> List[Tuple]:
    path: str = __csv_path
    logging.debug('Loading csv file %s', path)

    fs = open(path, 'r')

    csv_file = csv.reader(fs, delimiter=',')
    data: List = []
    for row in csv_file:
        data.append(row)

    logging.debug('Got %d rows', len(data))

    return data
