# Floyd-Warshall Algorithm

## Introduction
The Floyd-Warshall algorithm is a classic algorithm used to find the shortest paths between all pairs of nodes in a weighted graph.

## Implementation
This Python implementation of the Floyd-Warshall algorithm uses recursion to find the shortest paths between all pairs of nodes. The `floyd_warshall_recursive` function takes an adjacency matrix representation of the graph as input and returns the shortest distances between all pairs of nodes.

## Testing
The code includes a unit test case to verify the correctness of the `floyd_warshall_recursive` function. The test ensures that the function returns the expected shortest distances for a given input graph.

## Performance
The code also includes an example of profiling using `cProfile` to analyze the performance of the `floyd_warshall_recursive` function. Profiling can help identify performance bottlenecks and optimize the algorithm if needed.
