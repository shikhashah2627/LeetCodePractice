#  Hackerrank Graphs Questions
from queue import Queue
def roadsAndLibraries(n, c_lib, c_road, cities):
    total = 0
    if c_lib < c_road:
        total = n*c_lib
    else:       
        neighbours = {}
        visited = [False] * n
        connectedComponents = 0
        nodes_per_cluster = {}

        #recursive DFS
        def dfs(i,cluster):
            if not visited[i]:
                #check how many unique nodes are in this cluster
                nodes_per_cluster[cluster] = (
                    nodes_per_cluster.get(cluster,0) + 1)
            #mark this as visited
            visited[i] = True
            my_neighbours = []
            try:
                my_neighbours = neighbours[i+1] 
            except KeyError as ke:
                # we found a single node cluster (city with one house)
                # leave the list empty and the for-loop will skip it
                pass
            for city_id in my_neighbours:
                if not visited[city_id-1]:
                    dfs(city_id-1,cluster)

        #populate the adjacency list
        for road in cities:
            neighbours[road[0]] = (
                neighbours.get(road[0],[]) + [road[1]])
            neighbours[road[1]] = (
                neighbours.get(road[1],[]) + [road[0]])
        
        for i in range(n):
            if not visited[i]:
                dfs(i,i)
                connectedComponents += 1

        #min number of roads is always number of houses - 1      
        roads = sum(x-1 for x in nodes_per_cluster.values())
            
        total = c_road * roads + c_lib * connectedComponents
    return total
# n = 6 
# # cities = [[1, 3], [3 ,4], [2, 4], [1, 2], [2, 3], [5, 6]]
# c_lib = 2 
# c_road = 5
n = 3
cities = [[1, 2], [3, 1], [2, 3]]
c_lib = 2
c_road = 1
# print(roadsAndLibraries(n, c_lib, c_road, cities))

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    g = {i + 1: [] for i in range(graph_nodes)}
    for i in range(len(graph_from)):
        g[graph_from[i]].append(graph_to[i])
        g[graph_to[i]].append(graph_from[i])
    print("g:",g)
    target_nodes = []
    # print("ids:",ids) --> respective color
    # print("val",val) --> TargetColor
    for i in range(len(ids)):
        if ids[i] == val:
            target_nodes.append(i + 1)
    print("target:",target_nodes)
    result = -1
    for node in target_nodes:
        print("node:",node)
        w = weight(g, target_nodes, node, result)
        if w >0 and w < result or result == -1:
            result = w
    return result

def weight(g, target_nodes, node, limit=-1):
    visited = set()
    q = Queue()
    q.put((node, 0))
    while not q.empty():
        n, w = q.get()
        if n in visited:
            continue
        if n in target_nodes and n != node:
            return w
        visited.add(n)
        if w == limit:
            return -1
        for next_node in g[n]:
            if next_node not in visited:
                q.put((next_node, w + 1))
    return -1    
  
graph_nodes = 5 
graph_from = [1, 1, 2, 3]
graph_to = [2, 3, 4, 5]
ids = [1, 2, 3, 3, 2]
val = 2
# print(findShortest(graph_nodes, graph_from, graph_to, ids, val))
    
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = queue.Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(root)

        print (" ".join(map(str,distances)))
        

def maxRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion
            
def countCells(grid, i, j):
    if (not(i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count
    
# grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]    
# print(maxRegion(grid))



from collections import defaultdict
# Complete the minTime function below.
def minTime(roads, machines):
    parent = {} 
    dp = defaultdict(int)  #dp[i] denotes whether or not component with root i had already had a machine
    for machine in machines : dp[machine] = 1
    find = lambda node : node if parent.get(node, node) == node else find(parent[node])
    def union(i,j):
        x,y = find(i), find(j) 
        print("x:",x,"y:", y)
        if not dp[x] or not dp[y]:
            if i != x : x,y = y,x 
            parent[x] = y 
            dp[x] |= dp[y] 
            dp[y] |= dp[x] 
            return True
    return sum(time for i,j, time in sorted(roads, key = lambda i : -i[2]) if not union(i,j)) 

roads = [[1, 0, 5], [2, 1, 8], [2, 4, 5], [1, 3, 4]] 
machines = [2, 4, 0]
minTime(roads, machines)