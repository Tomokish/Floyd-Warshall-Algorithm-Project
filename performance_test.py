import sys

import cProfile
from Floyd import floyd_warshall_recursive;

NO_PATH = sys.maxsize

num_nodes = 10  # You can change the number of nodes for testing
graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0],
        ]
    
profiler = cProfile.Profile()
profiler.enable()
    
# Call the function you want to profile
floyd_warshall_recursive(graph)
 
profiler.disable()
profiler.print_stats()
