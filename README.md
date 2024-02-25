# Floyd-Warshall Algorithm

## Introduction
The Floyd-Warshall algorithm is an algorithm that is used to find the shortest paths between all pairs of nodes in a weighted graph and considering each node as an intermediate node.

## Implementation
This Python implementation of Floyd-Warshall algorithm uses recursion to find the shortest paths between all pairs of nodes. The `floyd_warshall_recursive` function takes an adjacency matrix representation of the graph as input and returns the shortest distances between all pairs of nodes.The output matrix was further tested with unit test and performance test.

## Testing
This code includes a unit test case to verify the accuracy of the `floyd_warshall_recursive` function. This test is to ensures that the function returns the expected shortest distances  value for a given input graph.

## Performance
The code also entails an example of profiling using `cProfile` to analyze the effectiveness and performance of the `floyd_warshall_recursive` function. Profiling can help identify performance bottlenecks and optimize the algorithm if needed.

# Requirement 
The requirement test is often used to list out the dependencies that is required for the code to work.