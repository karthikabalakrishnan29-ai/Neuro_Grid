import networkx as nx

class GraphOptimizer:
    def __init__(self, system_graph):
        self.system_graph = system_graph

    def find_shortest_path(self, start_node, end_node):
        """Power flow distance-a optimize panna"""
        try:
            path = nx.shortest_path(self.system_graph.graph, start_node, end_node)
            return path
        except nx.NetworkXNoPath:
            return None

    def check_islanding_status(self):
        """Utility grid cut aana, internal connectivity irukkanu check pannum"""
        # Logic to check if microgrid can survive offline
        is_connected = nx.has_path(self.system_graph.graph, "Source_Solar", "Load_Primary")
        return is_connected