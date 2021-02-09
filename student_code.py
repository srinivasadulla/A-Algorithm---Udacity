import math
import heapq
import copy

def shortest_path(M, start, goal):
    print("shortest path called")

    #Start point and goal are at same node
    if start == goal:
        return [start]
    
    
    h_cost = []      #Initializing heuristic cost list
    nodes = M.intersections
    visited = {}     #Initializing to keep track of visited nodes
    for i in range(len(M.intersections)):
        # calculate heuristic cost for all nodes and append to the list
        h = cost(nodes[i], nodes[goal])
        h_cost.append(h)
        visited[i] = 0
    
    # Inititalizing heap
    heap = []
    heapq.heappush(heap, [h_cost[start], 0, start])
    visited[start] = 1
    dest_paths = {}
    while len(heap)!=0:
        child_path = heapq.heappop(heap)
        curr_node = child_path[-1]
        if child_path[1] == 1:
            dest_paths[child_path[0]] = child_path[2::]
            continue
            
        for node in M.roads[curr_node]:
            if visited[node] == 1:
                continue
            else:
                g_c = cost(nodes[curr_node], nodes[node])
                h_c = h_cost[node]
                f = g_c + h_c
                temp_path = copy.deepcopy(child_path)
                temp_path[0] += f
                if node == goal:
                    temp_path[1] = 1
                temp_path.append(node)
                heapq.heappush(heap, temp_path)
        
        visited[curr_node] = 1

    return dest_paths[min(dest_paths)]


def cost(point1, point2):
    #This cost function provides Euclidean distance between two points
    dist = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
    
    return dist
