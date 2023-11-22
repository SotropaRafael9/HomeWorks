from Operations import *
from exception import GraphException


class UI:
    def __init__(self, file_path):
        try:
            self._file_path = file_path
            self._graph = read_graph(file_path)
        except FileNotFoundError:
            print("There is no such file.")

    def print_number_of_vertices(self):
        print(self._graph.number_vertices)

    def print_number_of_edges(self):
        print(self._graph.number_of_edges)

    def print_parse_vertices(self):
        vertices = ""
        for vertex in self._graph.parse_vertices():
            vertices += str(vertex) + " "
        print(vertices)

    def ui_find_edge(self):
        x = int(input("First vertex = "))
        y = int(input("Second vertex = "))
        print(self._graph.find_edge(x, y))

    def ui_add_edge(self):
        x = int(input("First vertex = "))
        y = int(input("Second vertex = "))
        cost = int(input("Cost of the edge = "))
        self._graph.add_edge(x, y, cost)

    def ui_remove_edge(self):
        x = int(input("First vertex = "))
        y = int(input("Second vertex = "))
        self._graph.remove_edge(x, y)

    def ui_add_vertex(self):
        x = int(input("Enter the new vertex: "))
        self._graph.add_vertex(x)

    def ui_remove_vertex(self):
        x = int(input("Enter the vertex you want to remove: "))
        self._graph.remove_vertex(x)

    def list_outbound_of_vertex(self):
        x = int(input("Enter the vertex: "))
        outbound = self._graph.parse_outbound(x)
        outbound_str = ""
        for vertex in outbound:
            outbound_str += str(vertex) + " "
        print(outbound_str)

    def list_inbound_of_vertex(self):
        x = int(input("Enter the vertex: "))
        inbound = self._graph.parse_inbound(x)
        inbound_str = ""
        for vertex in inbound:
            inbound_str += str(vertex) + " "
        print(inbound_str)

    def copy(self):
        new_copy = Graph.make_copy()
        print("Copy succesfully created ! ")
    
    def ui_get_degree_in(self):
        x = int(input("Enter the vertex: "))
        print("The in degree of vertex " + str(x) + " is: " + str(self._graph.get_degree_in(x)))

    def ui_get_degree_out(self):
        x = int(input("Enter the vertex: "))
        print("The out degree of vertex " + str(x) + " is: " + str(self._graph.get_degree_out(x)))

    

    def __str__(self):
        print(Graph.inbound)
        print(Graph.outbound)
        print(Graph.costs)
        return ""
    
    def print_graph(self):
        edges_list = Graph.get_list_of_edges(self._graph)
        for edge in edges_list:
            print(f"{edge[0]} {edge[1]} {edge[2]}")
        print()
        
    def ui_modify_cost(self):
        x = int(input("First vertex = "))
        y = int(input("Second vertex = "))
        cost = int(input("Input cost: "))
        self._graph.modify_cost(x, y, cost)

    def list_outbound_of_vertex_with_costs(self):
        x = int(input("Enter the vertex: "))
        outbound = self._graph.parse_outbound_with_costs(x)
        outbound_str = ""
        for vertex in outbound:
            outbound_str += str(vertex) + " "
        print(outbound_str)

    def list_inbound_of_vertex_with_costs(self):
        x = int(input("Enter the vertex: "))
        inbound = self._graph.parse_inbound_with_costs(x)
        inbound_str = ""
        for vertex in inbound:
            inbound_str += str(vertex) + " "
        print(inbound_str)

    def ui_get_connected_comps(self):
        connected_comp = self._graph.get_connected_components()
        for component in connected_comp:
            component_string = "New component: "
            for vertex in component:
                component_string += str(vertex) + " "
            print(component_string)
    def ui_get_find_shotes_path(self):
        start = int(input("start"))
        end = int(input("end"))
        path = lowest_length_path(self._graph, start, end)
        if path != None:
            print("Path: ", *path)
            print(f"Length: {len(path)}")
        else:
            print("Path not found !")
    
    def ui_Dijkstra(self):
        start = int(input("Start: "))
        end = int(input("End: "))
        try:
            (dist, prev) = self._graph.find_the_lowest_cost_walk(start, end)
            print(dist)
            walk = []
            while end != start:
                walk.append(end)
                end = prev[end]
            walk.append(end)
            walk.reverse()
            for vertex in walk:
                print(vertex)

        except Exception as e:
            print(e)
    def ui_Prims_algorithm(self):
        start = int(input("Start: "))
        try:
            msTree = self._graph.msp_prim(start)
            print(msTree)
        except Exception as e:
            print(e)


    def print_menu(self):
        print("\n1. Get the number of vertices :")
        print("2. Get the number of edges :")
        print("3. Parse vertices : ")
        print("4. Find edge : ")
        print("5. Add edge : ")
        print("6. Remove edge : ")
        print("7. Add vertex :")
        print("8. Remove vertex :")
        print("9. List the outbound of a vertex :")
        print("10. List the inbound of a vertex :")
        print("11. List the outbound costs of a vertex : ")
        print("12. List the inbound costs of a vertex : ")
        print("13. Get degree in :")
        print("14. Get degree out : ")
        print("15. Modify cost : ")
        print("16. Print graph : ")
        print("17. find the shortest path starting from the end")
        print("18. Dijkstra : ")
        print("19. Prim's algorithm: ")
        print("0. Exit.\n")


    def run_console(self):
        while True:
            try:

                self.print_menu()
                command = int(input("Choose your option: "))

                if command == 1:
                    self.print_number_of_vertices()
                elif command == 2:
                    self.print_number_of_edges()
                elif command == 3:
                    self.print_parse_vertices()
                elif command == 4:
                    self.ui_find_edge()
                elif command == 5:
                    self.ui_add_edge()
                elif command == 6:
                    self.ui_remove_edge()
                elif command == 7:
                    self.ui_add_vertex()
                elif command == 8:
                    self.ui_remove_vertex()
                elif command == 9:
                    self.list_outbound_of_vertex()
                elif command == 10:
                    self.list_inbound_of_vertex()
                elif command == 11:
                    self.list_outbound_of_vertex_with_costs()
                elif command == 12:
                    self.list_inbound_of_vertex_with_costs()
                elif command == 13:
                    self.ui_get_degree_in()
                elif command == 14:
                    self.ui_get_degree_out()
                elif command == 15:
                    self.ui_modify_cost()
                elif command == 16:
                    self.print_graph()
                elif command == 17:
                    self.ui_get_find_shotes_path()
                elif command == 18:
                    self.ui_Dijkstra()
                elif command == 19:
                    self.ui_Prims_algorithm()
                elif command == 0:
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid input.")
            except GraphException as ge:
                print(ge.get_message())