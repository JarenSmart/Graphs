from projects.graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # empty graph to work with
    family_tree = Graph()

    # add in items to graph above
    for family_pair in ancestors:
        family_tree.Graph.add_vertex(family_pair[0])
        family_tree.add_vertex(family_pair[1])
        family_tree.add_edge(family_pair[1], family_pair[0])

    if not family_tree.vertices[starting_node]:
        return -1  # if the input doesn't have any 'parents' -> return -1
    else:
        main_path = family_tree.dft(starting_node)
        first_children = main_path[-2]
        lowest_point = main_path.pop()
        for parent in family_tree.get_neighbors(first_children):
            if parent < lowest_point:
                lowest_point = parent
        return lowest_point
