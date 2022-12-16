from enum import Enum, verify, UNIQUE


@verify(UNIQUE)
class Areas(Enum):
    PHARMACY = 1
    PERFUMERY = 2
    COSMETICS = 3
    TOYS = 4

