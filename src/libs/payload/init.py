import logging

from typing import List
from typing import Tuple

from . import __column_choice as choice
from . import __column_data as cold
from . import __column_names as names
from . import __data as data


def exec() -> None:
    dump: List[Tuple] = data.exec()
    logging.debug("Got data, size='%s'", len(str(dump)))

    cleaned: List[cold.MyData] = choice.exec(dump)

    title: List[str] = names.exec()
    logging.debug("Column titles: %s", str(title))
