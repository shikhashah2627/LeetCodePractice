#  Hackerrank Graphs Questions
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
print(roadsAndLibraries(n, c_lib, c_road, cities))    
    