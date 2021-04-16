from __future__ import annotations


from Point import Point, from_two_points


class Edge:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.vertex1 = p1
        self.vertex2 = p2
        self.point1 = from_two_points(p1, p2)
        self.point2 = from_two_points(p2, p1)

    def __str__(self) -> str:
        return f"{self.vertex1} --- {self.vertex2}"

    def reversed(self) -> Edge:
        return Edge(self.vertex2, self.vertex1)

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.vertex1, self.vertex2))

    def __eq__(self, other: Edge) -> bool:
        return hash(self) == hash(other) or hash(self) == hash(other.reversed())
