import heapq



def uniform_cost_search(graph, start, goal):

    # Keep track of the cost of reaching each node

    cost = {start: 0}



    # Keep track of the nodes visited

    visited = set()



    # Use a priority queue to order the nodes to be explored

    priority_queue = [(0, start)]



    while priority_queue:

        # Get the node with the lowest cost

        (current_cost, current_node) = heapq.heappop(priority_queue)



        # Check if the current node is the goal

        if current_node == goal:

            return current_cost



        # Skip the node if it has already been visited

        if current_node in visited:

            continue

        visited.add(current_node)



        # Explore the neighbors of the current node

        for neighbor, weight in graph[current_node].items():

            # Calculate the cost of reaching the neighbor

            new_cost = current_cost + weight



            # Update the cost if it's lower than the previous cost

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                heapq.heappush(priority_queue, (new_cost, neighbor))



    return None



graph = {

    'A': {'B': 1, 'C': 4},

    'B': {'A': 1, 'C': 2, 'D': 5},

    'C': {'A': 4, 'B': 2, 'D': 1},

    'D': {'B': 5, 'C': 1}

}

start = 'A'

goal = 'D'

print("Cost of the path:", uniform_cost_search(graph, start, goal))

