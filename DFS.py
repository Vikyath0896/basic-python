def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        node = input("Enter the node: ")
        neighbors_str = input("Enter the neighbors (comma-separated): ")
        neighbors = neighbors_str.split(',') if neighbors_str else [] 
        graph[node] = neighbors

    return graph
def dfs(visited, graph, node): 
    if node not in visited:
        print(node) 
        visited.add(node)
        for neighbour in graph[node]: 
            dfs(visited, graph, neighbour)

# Driver Code
graph = input_graph()
visited = set() # Set to keep track of visited nodes of graph. 
start_node = input("Enter the starting node for DFS: ")
print("Following is the Depth-First Search") 
dfs(visited, graph, start_node)




