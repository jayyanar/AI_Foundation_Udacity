##In A* We Use both the below techniques
#1) Favoring nodes that are close to the starting point 2)Favoring nodes that are close to the goal f(n) --> fScore
#f(n) = g(n) + h(n).

import math
from queue import PriorityQueue


## Calculate Euclidean distance for graph (x1,y1) to (x2,y2) https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions
##h(n) represents the heuristic estimated cost from node n to the goal. -- distance_value

def euclidean_distance(start, destination):
    distance_value = math.sqrt(((start[0] - destination[0]) ** 2) + ((start[1] - destination[1]) ** 2))
    return distance_value

# Check the not is explored and meet the goal 
#1) Check the current node (testcase2) is destination if yes set shortestpath is
#2) if the Frontiernode is not start node, take the previous node and move the node to shortestpath and reverse for ascending

def traversepath(previous_node, start, destination):
    current_node = destination
    shortest_path = [current_node]
    while current_node != start:
        current_node = previous_node[current_node]
        shortest_path.append(current_node)
    shortest_path.reverse()
    return shortest_path


#Problem Solving

#Input - set of map intersection (40)
#Output - Find a optimal path of Point A to B using A*

#Usage of heuristic
#ref : https://www.redblobgames.com/pathfinding/a-star/implementation.html
#ref : https://www.redblobgames.com/pathfinding/a-star/introduction.html#dijkstra

#heuristic function h(n) tells A* an estimate of the minimum cost from any node n to the goal. It’s important to choose a good heuristic function.
#If heuristic =< 0, Then g(n) then A* guaranteed to find a shortest path.
#if heuristic > 0 then A* doesn't guaranteed to find a shortest path
#At the other extreme, if h(n) is very high relative to g(n), then only h(n) plays a role, and A* turns into Greedy Best-First-Search.

#Action/Code steps:

#Need to have two sets 1) Frontier 2) Explored and each node keeps a pointer to its parent in order to determine how it was Found
#1) Frontier will contain only one element, which is starting element and then select the candidates for examining.
#2) Explored set contains the list of nodes already been examined., Initially it will be empty
#3) Create a loop that repeatedly check the frontier node with lowest f value. if current(n) is the goal then we completed; if not, keep adding to the explored #and then its neighbours will be examined,
#4) If neighbor already examined, no need to check or else add to Frontier 


def shortest_path(M, start, goal):
    frontier = PriorityQueue() #Initiate the Priority queue # Entries are kept sorted and the lowest valued entry is retrieved first.
    frontier.put(start, 0) #keep the maxsizeis 0, he queue size is infinite. and start with initial Node
    previous_node = {start: None} 
    total_cost = {start: 0}       

    while not frontier.empty():
        current_node = frontier.get() # If the frontier is empty get the next node via get.

        if current_node == goal:
            print (traversepath(previous_node, start, goal))
            print ("Destination Reached")
            traversepath(previous_node, start, goal)
          
        for neighbor in M.roads[current_node]:
            new_cost = total_cost[current_node] + euclidean_distance(M.intersections[current_node], M.intersections[neighbor])

            if neighbor not in total_cost or new_cost < total_cost[neighbor]:
                total_cost[neighbor] = new_cost
                fScore = new_cost + euclidean_distance(M.intersections[current_node], M.intersections[neighbor])
                frontier.put(neighbor, fScore)
                previous_node[neighbor] = current_node
    return traversepath(previous_node, start, goal)