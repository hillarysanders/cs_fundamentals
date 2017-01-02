#######################################################################################################################
# module containing objects and functions relating to graphs and trees.
#######################################################################################################################
from collections import defaultdict

class Graph:
    """
    This class represents a directed graph using adjacency
    list representation
    """
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_traversal(self, start_node=0):
        """
        Assuming you're starting at a point that can get to all other points in the graph:
        - instantiate a 'been there' list of traversed nodes, starts with just our start node.
        1. list all nodes adjacent from your current node
        2. add all sudes that are not already in your queue (a TODO list) and haven't yet been traversed
        3. For each node in your queue, repeat step 1., 2, and 3. If there are no nodes left, stop.
        """

        # it would be faster if this was a dict, but we want to maintain ordering for final return object
        traversed_list = [start_node]
        traversed_dict = {start_node: False}
        queue = [start_node]

        while queue:
            node = queue.pop(0)
            adj = self.graph[node]
            new_traversals = [t for t in adj if not traversed_dict.has_key(t)]
            for t in new_traversals:
                traversed_dict[t] = True
            traversed_list.extend(new_traversals)
            queue.extend(new_traversals)

        return traversed_list


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print "Following is Breadth First Traversal (starting from vertex 2)"
g.breadth_first_traversal(2)

