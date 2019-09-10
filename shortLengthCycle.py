import sys
from collections import defaultdict, deque

class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
  
   
    # function to add an edge to graph 
    def addEdge(self,v,w): 
        self.graph[v].append(w) #Add w to v_s list 
        self.graph[w].append(v) #Add v to w_s list 
    
    def shortLengthCycle(self, n):
        maxLen = 109999999
        totalELemenents = n
        for i in range(n):
            dist = [0.000000001] * totalELemenents
            parent = [-1] * totalELemenents
            dist[i] = 0
            q = deque()
            q.append(i)
            while q:
                n = len(q)
                ele = q.pop()
                for j in self.graph[ele]:
                    # if the child is not visited
                    if dist[j] == 0.000000001:
                        q.append(j)
                        dist[j] = dist[ele] + 1
                        parent[j] = ele
                    elif parent[j] != ele and parent[ele] != j:
                        maxLen = min(maxLen, dist[j] + dist[ele] + 1)
        return maxLen
                        
                        
                    
        
        
        
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(1, 2)
g.addEdge(2, 5)
g.addEdge(2, 3)
g.addEdge(3, 4)
print(g.shortLengthCycle(6))


