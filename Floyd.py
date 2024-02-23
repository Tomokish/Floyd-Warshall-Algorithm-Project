import sys

NO_PATH = sys.maxsize

def floyd_warshall_recursive(graph):
    """
    Floyd-Warshall algorithm to find the shortest paths between all pairs of nodes using recursion.
    
    Args:
    graph (list of lists): The adjacency matrix representation of the graph.
    
    Returns:
    list of lists: The shortest distances between all pairs of nodes.
    """
    num_nodes = len(graph)
    
    def helper(distance, intermediate_node, start_node, end_node):
        """
        Helper function for recursive computation of shortest distances.
        """
        if intermediate_node >= num_nodes:
            return
        
        if start_node == num_nodes:
            return helper(distance, intermediate_node + 1, 0, 0)
        
        if end_node == num_nodes:
            return helper(distance, intermediate_node, start_node + 1, 0)
        
        if start_node == end_node:
            return helper(distance, intermediate_node, start_node, end_node + 1)
        
        if distance[start_node][intermediate_node] + distance[intermediate_node][end_node] < distance[start_node][end_node]:
            distance[start_node][end_node] = distance[start_node][intermediate_node] + distance[intermediate_node][end_node]
        
        return helper(distance, intermediate_node, start_node, end_node + 1)

    # Initialize distance matrix with the same values as the adjacency matrix
    distance = [row[:] for row in graph]

    helper(distance, 0, 0, 0)

    return distance

# Example usage:
graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0],
        ]

shortest_distances = floyd_warshall_recursive(graph)
for row in shortest_distances:
    print(row)
