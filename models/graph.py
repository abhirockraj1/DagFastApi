# pydantic_models.py
from pydantic import BaseModel, Field
from typing import Dict, List, Hashable, Set
from collections import deque

class GraphReqBody(BaseModel):
    """
    Pydantic model for the incoming graph request body.
    """
    graph: Dict[Hashable, List[Hashable]] = Field(
        ...,
        description="Adjacency list representation of the graph."
    )

    # Methods to calculate graph properties (copied from previous response)
    def get_num_nodes(self) -> int:
        nodes = set(self.graph.keys())
        for neighbors in self.graph.values():
            for neighbor in neighbors:
                nodes.add(neighbor)
        return len(nodes)

    def get_num_edges(self) -> int:
        num_edges = 0
        for node, neighbors in self.graph.items():
            num_edges += len(neighbors)
        return num_edges

    def is_dag(self) -> bool:
        num_nodes = self.get_num_nodes()
        in_degree: Dict[Hashable, int] = {node: 0 for node in self.graph.keys()}

        all_graph_nodes = set(self.graph.keys())
        for neighbors_list in self.graph.values():
            for neighbor in neighbors_list:
                all_graph_nodes.add(neighbor)

        for node_id in all_graph_nodes:
            in_degree[node_id] = in_degree.get(node_id, 0) # Initialize or keep existing

        for neighbors in self.graph.values():
            for neighbor in neighbors:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1


        queue = deque([node for node, degree in in_degree.items() if degree == 0])

        count_visited_nodes = 0
        while queue:
            current_node = queue.popleft()
            count_visited_nodes += 1

            for neighbor in self.graph.get(current_node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count_visited_nodes == num_nodes


class GraphResBody(BaseModel):
    """
    Pydantic model for the outgoing graph analysis response.
    """
    num_nodes: int = Field(..., description="The total number of nodes in the graph.")
    num_edges: int = Field(..., description="The total number of directed edges in the graph.")
    is_dag: bool = Field(..., description="True if the graph is a Directed Acyclic Graph (DAG), False otherwise.")