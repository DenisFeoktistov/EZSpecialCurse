from typing import List, Union
from enum import Enum


from Edge import Edge
from Point import Point


class Face:
    class SIDES(Enum):
        ONE = 1
        TWO = 2

    def __init__(self, edges: List[Edge]) -> None:
        vertices = list(set((edges[0].vertex1, edges[0].vertex2, edges[1].vertex2, edges[1].vertex2)))
        self.vertex = vertices[0]
        self.normal = (vertices[1] - vertices[0]) % (vertices[2] - vertices[0])

        self.edges = edges

    def __contains__(self, x: Union[Point, Edge]) -> bool:
        if isinstance(x, Point):
            p = x
            return (p - self.vertex) * self.normal == 0
        elif isinstance(x, Edge):
            e = x
            return e.vertex1 in self and e.vertex2 in self
        return NotImplemented

    def side(self, p: Point) -> SIDES:
        return Face.SIDES.ONE if self.normal * (p - self.vertex) > 0 else Face.SIDES.TWO

    def __str__(self) -> str:
        return f"{self.edges}"

    def __repr__(self) -> str:
        return str(self)
