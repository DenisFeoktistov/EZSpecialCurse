from __future__ import annotations
from typing import Union
from math import sqrt


class Point:
    id = 0

    def __init__(self, x: int = 0, y: int = 0, z: int = 0, from_input=False) -> None:
        if not from_input:
            self.x = x
            self.y = y
            self.z = z
        else:
            self.x = int(input("Enter x: "))
            self.y = int(input("Enter y: "))
            self.z = int(input("Enter z: "))

        self.id = Point.id
        Point.id += 1

    def __neg__(self) -> Point:
        return Point(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        return sqrt(self * self)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point) -> Point:
        return self + (-other)

    def __mul__(self, other: Union[int, Point]) -> Union[Point, int]:
        if isinstance(other, int):
            return Point(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return NotImplemented

    def __mod__(self, other: Point) -> Point:
        return Point(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.x)

    def __iadd__(self, other: Point) -> None:
        self = self + other

    def __isub__(self, other: Point) -> None:
        self = self - other

    def __imod__(self, other: Point) -> None:
        self = self % other

    def __imul__(self, other: Union[int, Point]) -> None:
        self = self * other

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return str(self)


def from_two_points(p1: Point, p2: Point) -> Point:
    return Point(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

