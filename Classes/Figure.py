import json
import os
from typing import List, Dict

from Edge import Edge
from Face import Face
from Point import Point
from Subsidiary import enumerate_choice


class Figure:
    FILE_MODE = "Read from template file"
    CONSOLE_MODE = "Read from console"
    DIRECTORY_PATH = "../figures/"

    def __init__(self) -> None:
        self.vertices: List[Point] = list()
        self.edges: List[Edge] = list()
        self.edges_indices_dict: Dict[Edge, int] = dict()
        self.edges_vertices_dict: Dict[Point, List[Edge]] = dict()
        self.faces: List[Face] = list()

        self.reading_mode = enumerate_choice([Figure.FILE_MODE, Figure.CONSOLE_MODE],
                                             select_text="Select reading mode: ")
        if self.reading_mode == Figure.FILE_MODE:
            self.get_from_file()
        else:
            self.get_vertices()

            self.get_edges()

        self.init_edges_dict()
        self.init_faces()

    def init_edges_dict(self) -> None:
        for i, edge in enumerate(self.edges):
            self.edges_indices_dict[edge] = i

            if edge.vertex1 not in self.edges_vertices_dict.keys():
                self.edges_vertices_dict[edge.vertex1] = [edge]
            else:
                self.edges_vertices_dict[edge.vertex1].append(edge)

            if edge.vertex2 not in self.edges_vertices_dict.keys():
                self.edges_vertices_dict[edge.vertex2] = [edge.reversed()]
            else:
                self.edges_vertices_dict[edge.vertex2].append(edge.reversed())

    def get_from_file(self) -> None:
        file_name = enumerate_choice(os.listdir(Figure.DIRECTORY_PATH), select_text="Select file: ")

        with open(Figure.DIRECTORY_PATH + file_name) as file:
            data = json.load(file)

        for vertex in data["vertices"]:
            self.vertices.append(Point(vertex[0], vertex[1], vertex[2]))

        for i, edge in enumerate(data["edges"]):
            self.edges.append(Edge(self.vertices[edge[0]], self.vertices[edge[1]]))

    def get_vertices(self) -> None:
        n = int(input("Enter number of points: "))
        print()

        for i in range(n):
            print(f"Point {i + 1}: ")
            p = Point(from_input=True)
            print()
            self.vertices.append(p)

    def get_edges(self) -> None:
        m = int(input("Enter number of edges: "))

        print()
        print("\n".join(map(lambda i: f"Point {i + 1}: {self.vertices[i]}", range(len(self.vertices)))))
        print()

        for i in range(m):
            a, b = [int(x) for x in input("Enter indices of edge points: ").split()]
            print()
            self.edges.append(Edge(self.vertices[a - 1], self.vertices[b - 1]))

    def init_faces(self) -> None:
        for i, edge1 in enumerate(self.edges):
            for j, edge2 in enumerate(self.edges_vertices_dict[edge1.vertex2]):
                if edge1 == edge2:
                    continue

                flag = False
                for face in self.faces:
                    if edge1 in face and edge2 in face:
                        flag = True
                        break
                if flag:
                    continue

                self.faces.append(Face([edge1, edge2]))

                act_face = self.faces[-1]
                act_edge = edge2
                while not act_edge.vertex2 == edge1.vertex1:
                    for edge3 in self.edges_vertices_dict[act_edge.vertex2]:
                        if edge3 != act_edge and edge3 in act_face:
                            act_face.edges.append(edge3)
                            act_edge = edge3
                            break

    def main_method(self) -> None:
        face = enumerate_choice(self.faces, "Select face: ")
        edge = enumerate_choice(face.edges, "Select edge: ")
        for face2 in self.faces:
            if face != face2 and edge in face2:
                print(f"Bordering face: {face2}\n")
