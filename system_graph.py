import networkx as nx
from utils.logger import logger

class SystemGraph:
    def __init__(self):
        self.graph = nx.DiGraph() # Directed Graph for power flow
        self._initialize_nodes()

    def _initialize_nodes(self):
        """Microgrid components and their electrical connections"""
        # Nodes: (ID, Type, Capacity/Rating)
        self.graph.add_node("Source_Solar", type="DER", capacity=20.0)
        self.graph.add_node("Source_Wind", type="DER", capacity=15.0)
        self.graph.add_node("Battery_Unit", type="Storage", capacity=50.0)
        self.graph.add_node("Main_Bus", type="Busbar")
        self.graph.add_node("Load_Primary", type="Consumer")
        self.graph.add_node("Utility_Grid", type="Grid_Connection")

        # Edges: Power flow paths
        self.graph.add_edge("Source_Solar", "Main_Bus")
        self.graph.add_edge("Source_Wind", "Main_Bus")
        self.graph.add_edge("Main_Bus", "Battery_Unit")
        self.graph.add_edge("Battery_Unit", "Main_Bus") # Bidirectional
        self.graph.add_edge("Main_Bus", "Load_Primary")
        self.graph.add_edge("Main_Bus", "Utility_Grid")
        
        logger.info("System Graph (Topology) successfully initialized.")

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))