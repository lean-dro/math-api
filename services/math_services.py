from typing import List
from model.DemandsEnum import DemandsEnum


def resolve(list: List[float], type: DemandsEnum):
    match (type):
        case DemandsEnum.SUM:
            return sum(list)
            


def sum(list: List[float]):
    total = 0
    for number in list:
        total += number
    return total