import logging

from typing import List
from typing import Tuple

from . import __column_choice as choice
from . import __column_data as cold
from . import __data as data


def exec() -> None:
    dump: List[Tuple] = data.exec()
    logging.debug("Got data, size='%s'", len(str(dump)))

    cleaned: List[cold.MyData] = choice.exec(dump)
