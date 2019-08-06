# Hackerrank Tree Sums:

# Get the height of the tree.
def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1

# Find the lowest ancestor
def lca(root, v1, v2):
  #Enter your code here
    # Bigger than both
    if(root.info > v1 and root.info > v2):
        return lca(root.left,v1,v2)
    elif(root.info < v1 and root.info < v2):
        return lca(root.right,v1,v2)
    else: return root
    
# Check whether it's BST
import sys
def check(root, min, max):
    if root == None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)
def check_binary_search_tree_(root):
    return check(root, float('-inf'), float('inf'))
    
# Tree: Huffman Decoding
temp=root
    string=[]
    for i in s:
        c=int(i)
        if c==1:
            temp=temp.right
        elif c==0:
            temp=temp.left
        if temp.right==None and temp.left==None:
            string.append(temp.data)
            temp=root
    b=''.join(string)
    print b
    
# Balanced Forest
from collections import defaultdict, deque
# Complete the balancedForest function below.
def balancedForest(c, edges):
    if edges==[]:
        return -1

    #build a graph
    n=len(c)+1
    graph=defaultdict(list)
    root_max=0
    root_node=None
    for n1,n2 in edges:
        graph[n1].append(n2)
        if len(graph[n1])>root_max:
            root_max=len(graph[n1])
            root_node=n1
        graph[n2].append(n1)
        if len(graph[n2])>root_max:
            root_max=len(graph[n2])
            root_node=n2

    #BFS costs for root_node !!!!deque is mandatory for performance
    parent=[None]*n
    visited=[None]*n
    visited[root_node]=0
    S=deque([root_node])
    while len(S)>0:
        cur=S.popleft()
        visited_cur=visited[cur]
        for node in graph[cur]:
            if visited[node]!=None:
                continue
            S.append(node)
            visited[node]=visited_cur+1
            parent[node]=cur

    #build a tree
    sums=[None]
    sums.extend(c)
    for node,level in sorted([(i,visited[i]) for i in range(n) if visited[i]!=None],key=lambda x:x[1],reverse=True):
        if parent[node]!=None:
            sums[parent[node]]+=sums[node]

    #calculate constraints
    root_sum=sums[root_node] #R=root_sum=X+X+Y, X-big subtree, Y-small subtree
    lim1=math.ceil(root_sum/3)
    lim2=root_sum//2

    ##brute force: First Node with lim1<=X<=lim2
    S1=[i for i in range(n) if i!=root_node and sums[i]!=None and lim1<=sums[i]<=lim2]

    ##brute force: Second Node vals: X=R/2, X & R-2X dif subtree, 2X & R-X same subtree
    res=[]
    min_add_val=None
    for s1 in S1:
        val1=sums[s1]
        ### case X=R/2 exactly. Next, add same node with val1
        if root_sum==val1*2:
            if min_add_val==None or min_add_val>val1:
                min_add_val=val1
            continue

        ### case Split tree for 3 parts
        for i in range(n):
            if i not in (root_node,s1) and sums[i]!=None and sums[i] in (root_sum-val1*2,val1,val1*2,root_sum-val1):
                if min_add_val==None or min_add_val>3*val1-root_sum:
                    min_add_val=3*val1-root_sum
                break

    ##brute force: Third Node with lim1<= R-X <=lim2
    S3=[i for i in range(n) if i!=root_node and sums[i]!=None and lim1<=root_sum-sums[i]<=lim2]

    ##brute force: Forth Node vals: R-2X
    for s3 in S3:
        val1=sums[s3]
        S4=[i for i in range(n) if i not in (root_node,s3) and sums[i]!=None and sums[i]==val1*2-root_sum]
        for s4 in S4:
            cur=parent[s4]
            while cur!=None and cur!=s3:
                cur=parent[cur]
            val2=sums[s4]
            if cur==s3 and val2==2*val1-root_sum :
                if min_add_val==None or min_add_val>val1-val2*2:
                    min_add_val=val1-val2*2

    return -1 if min_add_val==None else min_add_val