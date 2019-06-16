from typing import List
import math

Vector = List[float]


def vector_length(a: Vector) -> float:
    square_sum = 0
    for comp in a:
        square_sum += comp ** 2
    return math.sqrt(square_sum)


def vector_addition(a: Vector, b: Vector) -> Vector:
    return [a[0]+b[0], a[1]+b[1]]


def vector_multiplication_by_k(k: float, a: Vector) -> Vector:
    return [k*a[0], k*a[1]]
