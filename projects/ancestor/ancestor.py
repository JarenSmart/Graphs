# from projects.graph import Graph


# def earliest_ancestor(ancestors, starting_node):
#     # empty graph to work with
#     family_tree = Graph()

#     # add in items to graph above
#     for family_pair in ancestors:
#         family_tree.Graph.add_vertex(family_pair[0])
#         family_tree.add_vertex(family_pair[1])
#         family_tree.add_edge(family_pair[1], family_pair[0])

#     if not family_tree.vertices[starting_node]:
#         return -1  # if the input doesn't have any 'parents' -> return -1
#     else:
#         main_path = family_tree.dft(starting_node)
#         first_children = main_path[-2]
#         lowest_point = main_path.pop()
#         for parent in family_tree.get_neighbors(first_children):
#             if parent < lowest_point:
#                 lowest_point = parent
#         return lowest_point

"""
Earliest Ancestor
Write a function that, given the dataset and the ID of an individual in the dataset,
returns their earliest known ancestor – the one at the farthest distance from the input individual.
If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
If the input individual has no parents, the function should return -1.
​
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
​
 Example input
  6
​
  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
"""


def earliest_ancestor(ancestors, starting_node):
    # Turn the ancestors list into an adjacency list
    adjacency_list = {}

    for ancestor_pair in ancestors:
       # add both vertices to adjacency_list
        if ancestor_pair[0] not in adjacency_list:
            adjacency_list[ancestor_pair[0]] = set()
        if ancestor_pair[1] not in adjacency_list:
            adjacency_list[ancestor_pair[1]] = set()
        # add the edge between the two vertices
        adjacency_list[ancestor_pair[1]].add(ancestor_pair[0])
    print(adjacency_list)
    # Create a queue
    queue = [[starting_node]]
    # create a visited set of vertices
    visited = set()
    max_path_length = 1
    current_earliest_ancestor = -1

    while len(queue) > 0:
        # dequeue the current path + vertex
        current_path = queue.pop(0)
        # get the current vertex out of the path
        current_vertex = current_path[-1]
        # if the vertex has not been visited
        if current_vertex not in visited:
            # add the vertex to the visited set
            visited.add(current_vertex)
            print(current_path)
            if len(current_path) > max_path_length or len(current_path) >= max_path_length and current_vertex < current_earliest_ancestor:
                max_path_length = len(current_path)
                current_earliest_ancestor = current_vertex
    # explore the neighbors
    # add the neighbor vertices to the queue (make sure to build the new paths)
            for neighbor in adjacency_list[current_vertex]:
                # copy the current path
                new_path = list(current_path)
                # add the neighbor to it
                new_path.append(neighbor)
                queue.append(new_path)
    return current_earliest_ancestor
