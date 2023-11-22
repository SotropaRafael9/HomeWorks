from asyncio import PriorityQueue
from exception import GraphException
from copy import deepcopy
from collections import deque
import random
import heapq
import sys
from queue import PriorityQueue

class Graph:
    _inbound : list
    _outbound : list
    _costs : list
    def __init__(self, vertices):

#        verices - iterable of vertices [1,2,3,4,5,6]
#        edges - iterable of tuples
#       [(1,2, 5), (6,4, -3), (3,1, 18), (2,2, 6), (5,3,4)]

        self._outbound = dict()  # a dictionary that stores the outbound neighbours for a vertex
        self._inbound = dict()  # a dictionary that stores the inbound neighbours for a vertex
        self._costs = dict()  # a dictionary that stores the costs for an edge
        self._edge_id = dict()

        for vertex in range(vertices) :
            self._outbound[vertex] = []
            self._inbound[vertex] = []

        # for x, y, z in edges:
        #     self._outbound[x].append(y)
        #     self._inbound[y].append(x)
        #     self._costs[(x, y)] = z

    def is_edge(self, x, y):
        # a function that verifies if there is an edge between x and y (x,y - vertices)
        if x in self._outbound:
            if y in self._outbound[x]:
                return True
        return False
    def is_vertex(self, vertex:int) -> bool:
        return vertex < len(self._inbound) and vertex >=0
        
    @property
    def outbound(self):
        return self._outbound

    @property
    def inbound(self):
        return self._inbound
    
    def get_edge_id(self, x, y) -> int:
        return self._edge_id[(x, y)]

    @property
    def number_vertices(self) -> int:
        # a function that returns the number of vertices
        return len(self._outbound)

    @property
    def number_of_edges(self):
        # a function that returns the number of edges
        return len(self._costs)

    @property
    def costs(self):
        # a function that returns the dictionary of costs
        return self._costs

    def get_list_of_edges(self):
        edges = []
        for key, val in self._costs.items():
            edges.append((key[0], key[1], val))
        return edges[:]
    def get_vertices_count(self):
        return len(self._inbound)   
             
    def parse_vertices(self):
        # a function that returns an iterable of the vertices
        if len(self._outbound) == 0:
            raise GraphException("There aren't any vertices.")
        return list(range(self.get_vertices_count()))


    def find_edge(self, x, y):
        # a function that verifies if there is an edge between vertices x and y and returns the cost of it if yes or raises an exception otherwise
        if self.is_edge(x, y) is False:
            raise GraphException("There is no edge between these vertices.")
        return self._costs[(x, y)]

    def parse_outbound(self, vertex):
        # a function that returns an iterable of the outbound neighbours of vertex x or None if x is not a vertex
        if not self.is_vertex(vertex):
            raise GraphException("aaaa")
        return [(vertex, neighboar)for neighboar in self._outbound[vertex]]

    def parse_outbound_neighboar(self, vertex):
        if not self.is_vertex(vertex):
            raise GraphException("is not here")
        return self._outbound[vertex][:]


    def parse_inbound(self, x):
        # a function that returns an iterable of the inbound neighbours of vertex x or None if x is not a vertex
        if x not in self.parse_vertices():
            raise GraphException("The given value is not a vertex 1.")
        return [y for y in self._inbound[x]]

    def parse_outbound_with_costs(self, x):
        # a function that returns an iterable of the edge costs of the outbound neighbours of vertex x or None if x is not a vertex
        if x not in self.parse_vertices():
            raise GraphException("The given value is not a vertex 2.")
        return [self._costs[(x, y)] for y in self._outbound[x]]

    def parse_inbound_with_costs(self, x):
        # a function that returns an iterable of the edge costs of the inbound neighbours of vertex x or None if x is not a vertex
        if x not in self.parse_vertices():
            raise GraphException("The given value is not a vertex 3.")
        return [self._costs[(y, x)] for y in self._inbound[x]]

    def get_degree_out(self, x):
        # a function that returns the outbound degree of the vertex x if this one exists
        if x not in self._outbound:
            raise GraphException("The given value is not a vertex 4.")
        return len(self._outbound[x])

    def get_degree_in(self, x):
        # a function that returns the inbound degree of the vertex x if this one exists
        if x not in self._inbound:
            raise GraphException("The given value is not a vertex. 5")
        return len(self._inbound[x])

    def parse_inbound_neighbours(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception()
        return self.inbound[vertex][:]
    def add_vertex(self, x):
        # a function that adds a vertex to the graph
        if x in self.parse_vertices():
            raise GraphException("The given value is a vertex.6")
        self._outbound[x] = []
        self._inbound[x] = []

    def remove_vertex(self, x):
        # a function that removes a vertex from the graph
        if x not in self.parse_vertices():
            raise GraphException("The given value is not a vertex.7")

        for y in self.parse_vertices():
            if x in self.parse_outbound(y):
                del self._costs[(y, x)]
                self._outbound[y].remove(x)
            if x in self.parse_inbound(y):
                del self._costs[(x, y)]
                self._inbound[y].remove(x)
        self._inbound.pop(x)
        self._outbound.pop(x)

#complexity O(n log n)
    def find_the_lowest_cost_walk(self, vertex1 : int, vertex2 : int):
            if not self.is_vertex(vertex1):
                raise GraphException("the vertex {} doesn't exist!".format(vertex1))
            if not self.is_vertex(vertex2):
                raise GraphException("the vertex {} doesn't exist!".format(vertex2))
            
            q = PriorityQueue()

            prev = {vertex: -1 for vertex in self.parse_vertices()} 
            dist = {vertex: float('inf') for vertex in self.parse_vertices()} 
            dist[vertex1] = 0
            q.put((dist[vertex1], vertex1))
            found = False
            while not q.empty() and not found:
                (ceva, x) = q.get()
                if x == vertex2:
                    found = True
                for y in self._outbound[x]:
                    if dist[y] is float('inf') or dist[x] + self.get_cost(x, y) < dist[y]:
                        dist[y] = dist[x] + self.get_cost(x, y)
                        q.put((dist[y], y))
                        prev[y] = x
            if found is False:
                raise GraphException("no walk between {} and {}.".format(vertex1, vertex2))
            return (dist[vertex2], prev)
    



    # def reconstruct_cheapest_path(self, start_vertex, end_vertex, costs):
    #     path = [start_vertex]
    #     while path[-1] != end_vertex:
    #         # Get the lowest path cost neighboar
    #         minCost = float('infinity')
    #         minVertex = None
    #         for vertex in self.parse_inbound_neighbours(path[-1]):
    #             if costs[vertex] < minCost:
    #                 minCost = costs[vertex]
    #                 minVertex = vertex
    #         path.append(minVertex)
    #     path.reverse()
    #     return path

    # def find_lowest_cost_between_the_give_vertices(self, start_vertex, end_vertex):
    #    if not self.is_vertex(start_vertex) or not self.is_vertex(end_vertex):
    #        raise GraphException()
    #    #no path
    #    if (start_vertex == end_vertex):
    #        return [0, [start_vertex]]
    #    #Dijkstra's algorithm
    #    costs = [float('infinity') ] * (len(self._outbound)+1)
    #    found = [False] * (len(self._inbound))

       
    #     # The cost of the start vertex to all the vertexes is the cost of the edge.
    #    for vertex in self.parse_vertices():
    #     try:
    #             costs[vertex] = self.get_cost(start_vertex, vertex)
    #     except:
    #         pass

    #     # The first vertex is always found and has a cost of 0.
    #     costs [start_vertex] = 0
    #     found [start_vertex] = True
    #     for vertex in self .parse_vertices () :
    #     # Go trough all the not added vertexes and find the one with the lowest cost.
    #         minPosition = -1
    #         for position in self.parse_vertices () :
    #             if not found [position] and (minPosition == 1 or costs [position] < costs [minPosition]):
    #                 minPosition = position
    #             # If a minimum vertex has been found.
    #             if minPosition > - 1:
    #                 found [minPosition] = True
    #             # Update the cost of all the neighbours of the current vertex.
    #                 for neighbour in self.parse_outbound_neighboar(minPosition):
    #                     costs[neighbour] = min(costs[neighbour], costs[minPosition] + self.get_cost(minPosition, neighbour))
    #     return [costs[end_vertex], self.reconstruct_cheapest_path(start_vertex, end_vertex, costs)]
    
    def get_cost(self, source : int, target :int):
        if not self.is_vertex(source) or not self.is_vertex(target):
            raise Exception()
        return self._costs[(source), target]
    
    def set_edge_id(self, x, y):
        while True:
            current_edge_id = random.randint(1, 10**6)
            is_unique = True
            for val in self._edge_id.values():
                if current_edge_id == val:
                    is_unique = False
                    break
            if is_unique:
                break
      #  print("x, y:", x, y)
        self._edge_id[(x, y)] = current_edge_id

    def add_edge(self, x, y, cost):
        # a function that adds an edge to the graph where x and y are the vertices
        if self.is_edge(x, y):
            raise GraphException("There already is an edge between these vertices.")
        self._outbound[x].append(y)
        self._inbound[y].append(x)
        self._costs[(x, y)] = cost

    # self.set_edge_id(x, y)

        while True:
            current_edge_id = random.randint(1, 10**6)
            is_unique = True
            for val in self._edge_id.values():
                if current_edge_id == val:
                    is_unique = False
                    break
            if is_unique:
                break
        #print("x, y:", x, y)
        self._edge_id[(x, y)] = current_edge_id

    def remove_edge(self, x, y):
        # a function that removes an edge from the graph if it exists (where x and y are vertices)
        if self.is_edge(x, y) is False:
            raise GraphException("There is no edge between these vertices.")
        del self._costs[(x, y)]

        self._outbound[x].remove(y)
        self._inbound[y].remove(x)

    def make_copy(self):
        # a function that returns a copy of the graph
        return deepcopy(self)

    def modify_cost(self, x, y, cost):
        # a function that modifies the cost of an edge if it exists
        if self.is_edge(x, y) is False:
            raise GraphException("There is no edge between these vertices.")
        self._costs[(x, y)] = cost

    def msp_prim(self, start_vertex):
    # a function that returns a minimum spanning tree of the graph using Prim's algorithm
    
        if len(self._outbound) == 0:
            raise GraphException("There aren't any vertices.")  # Raise an exception if there are no vertices in the graph
            
        visited = [False] * len(self._outbound)  # Create a list to track visited vertices, initially all set to False
        visited[start_vertex] = True  # Mark the start_vertex as visited
        
        edges = []  # Initialize an empty list to store the edges of the minimum spanning tree
        
        while len(edges) < len(self._outbound) - 1:
            # Repeat until the number of edges in the MST is one less than the total number of vertices
            
            min_cost = float('inf')  # Initialize the minimum cost to infinity
            min_edge = None  # Initialize the minimum cost edge as None
            
            for vertex in self.parse_vertices():
                # Iterate over all vertices in the graph using the parse_vertices method
                
                if visited[vertex] is True:
                    # Check if the vertex has been visited
                    
                    for neighbour in self.parse_outbound_neighboar(vertex):
                        # Iterate over the neighbors of the current vertex using the parse_outbound_neighboar method
                        
                        if visited[neighbour] is False and self.get_cost(vertex, neighbour) < min_cost:
                            # Check if the neighbour has not been visited and the cost of the edge is smaller than the current minimum cost
                            
                            min_cost = self.get_cost(vertex, neighbour)  # Update the minimum cost
                            min_edge = (vertex, neighbour)  # Update the minimum cost edge
            
            if min_edge is None:
                raise GraphException("The graph is not connected.")  # Raise an exception if no minimum cost edge is found, indicating the graph is not connected
            
            edges.append(min_edge)  # Add the minimum cost edge to the edges list
            visited[min_edge[1]] = True  # Mark the second vertex of the minimum cost edge as visited
            
        return edges  # Return the list of edges representing the minimum spanning tree

def build_random_graph(number_of_vertices, number_of_edges):
    # A function that receives 2 integers (number_of_vertices and number_of_edges) and generates and returns a random graph.
   # if 2 * number_of_edges > number_of_vertices * (number_of_vertices - 1):
    #    return False
    edge_set = set()
    while len(edge_set) < number_of_edges:
        x = random.randrange(number_of_vertices)
        y = random.randrange(number_of_vertices)
        z = random.randint(-20, 120)
        edge_set.add((x, y, z))

    generated_graph = Graph(range(number_of_vertices), edge_set)

    return generated_graph

def lowest_length_path(graph, start_vertex, end_vertex):
    # Perform a backward breadth-first search starting from the ending vertex.
    queue = deque([end_vertex])
    visited = set([end_vertex])
    successors = {}

    while queue:
        current_vertex = queue.popleft()
        if current_vertex == start_vertex:
            break
        for neighbor in graph.parse_inbound(current_vertex):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                successors[neighbor] = current_vertex

    # Reconstruct the lowest length path from the start vertex to the end vertex.
    path = [start_vertex]
    current_vertex = start_vertex
    if start_vertex in successors:
        while current_vertex != end_vertex:
            next_vertex = successors[current_vertex]
            path.append(next_vertex)
            current_vertex = next_vertex
        #path.reverse()
        return path
    else:
        return None
    
    


def write_graph_to_file(graph, file_path):

#    A function that writes a given graph into a text file.
#   param graph: an object of class Graph
#    param file_path: a string representing the given file.

    f = open(file_path, "wt")
    first_line = str(graph.number_vertices) + " " + str(graph.number_of_edges) + "\n"
    f.write(first_line)
    if len(graph.parse_vertices()) == 0:
        raise ValueError("Can't write anything.")
    for edge in graph.costs:
        line = str(edge[0]) + " " + str(edge[1]) + " " + str(graph.find_edge(edge[0], edge[1])) + "\n"
        f.write(line)
    for vertex in graph.parse_vertices():
        if len(graph.outbound[vertex]) == 0 and len(graph.inbound[vertex]) == 0:
            line = str(vertex) + "\n"
            f.write(line)
    f.close()


def read_graph(file_path)->Graph:
    with(open(file_path, "r")as file):
        lines = file.readlines()
        [vertices, endge] = [int(element) for element in lines[0].split(' ')]
        result = Graph(vertices)
        for index in range(1, endge+1):
            result.add_edge(*[int(element)for element in lines[index].split(' ')]) 
        file.close()
        return result
    #a function that reads a graph from a given file path and returns an object of class Graph
    # f = open(file_path, "rt")
    # line = f.readline()
    # if len(line) < 3:
    #     raise ValueError("Number of vertices/edges is missing.")
    # edge_set = list()
    # elements = line.split()
    # vertices_nr = int(elements[0])
    # edges_nr = int(elements[1])
    # for line in f.readlines():
    #     if len(line) > 1:
    #         elements = line.split()
    #         out_vertex = int(elements[0])
    #         in_vertex = int(elements[1])
    #         cost = int(elements[2])
    #         edge_set.append((out_vertex, in_vertex, cost))

    # new_graph = Graph(range(vertices_nr), edge_set)
    # return new_graph

# def random_graph(number_of_vertices, number_of_edges):

#     if number_of_vertices **2 > number_of_edges:
#         return
#     new_graph = Graph()
#     for vertix in range(number_of_vertices):
        
#     index = 0
#     while index < number_of_edges:
        



