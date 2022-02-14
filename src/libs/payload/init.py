import logging

from typing import List
from typing import Tuple

from . import __data as data


def exec() -> None:
    dump: List[Tuple] = data.exec()
    logging.debug("Got data %s", str(dump))
