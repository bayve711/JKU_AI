from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


def get_solver_mapping():
    return dict(ucs=UCS)


class UCS(object):
    # TODO, excercise 2:
    # - implement Uniform Cost Search (UCS), a variant of Dijkstra's Graph Search
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - store visited nodes in a 'set()'
    def solve(self, problem: Problem):
        fringe = PriorityQueue()
        visited_nodes = set()
        expanded_nodes = set()
        initial_node = problem.get_start_node()
        fringe.put(0, initial_node)
        expanded_nodes.add(initial_node)

        while fringe.has_elements():
            cost, node = fringe.get(include_priority=True)
            expanded_nodes.remove(node)

            if problem.is_end(node):
                return node

            if node not in visited_nodes:
                visited_nodes.add(node)
                for node_1 in problem.successors(node):
                    if node_1 not in visited_nodes:
                        new_cost = cost + problem.action_cost(node.state, node_1.action)
                        if node_1 not in expanded_nodes:
                            fringe.put(new_cost, node_1)
                            expanded_nodes.add(node_1)
        return None
