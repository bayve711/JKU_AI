from .. problem import Problem
from .. datastructures.queue import Queue


# please ignore this
def get_solver_mapping():
    return dict(bfs=BFS)


class BFS(object):
    # TODO, exercise 1:
    # - use 'problem.get_start_node()' to get the node with the start state
    # - use 'problem.is_end(node)' to check whether 'node' is the node with the end state
    # - use a set() to store already visited nodes
    # - use the 'queue' datastructure that is already imported as the 'fringe'/ the 'frontier'
    # - use 'problem.successors(node)' to get a list of nodes containing successor states
    def solve(self, problem: Problem):
        current = problem.get_start_node()
        visited = set()
        fringe = Queue()
        if problem.is_end(current):
            return current
        fringe.put(current)
        visited.add(current)
        while len(fringe) > 0:
            node = fringe.get()
            for node_1 in problem.successors(node):
                if node_1 not in visited:
                    if problem.is_end(node_1):
                        return node_1
                    fringe.put(node_1)
                    visited.add(node_1)
        return None

