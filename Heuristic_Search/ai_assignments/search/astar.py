import math
from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


# please ignore this
def get_solver_mapping():
    return dict(
        astar_ec=ASTAR_Euclidean,
        astar_mh=ASTAR_Manhattan
    )


class ASTAR(object):
    # TODO, Exercise 2:
    # implement A* search (ASTAR)
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - use a 'set()' to store nodes that were already visited
    def solve(self, problem: Problem):
        fringe = PriorityQueue()
        first_node = problem.get_start_node()
        end_node = problem.get_end_node()

        fringe.put(0 + self.heuristic(first_node, end_node), first_node)
        visited = set()
        while len(fringe) > 0:
            current = fringe.get()
            if problem.is_end(current):
                return current
            visited.add(current)
            for successor in problem.successors(current):
                if successor not in visited and successor not in fringe:
                    cost = successor.cost + current.cost
                    fringe.put(cost + self.heuristic(successor, end_node), successor)
        return None



# please note that in an ideal world, the heuristics should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state


# this is the ASTAR variant with the euclidean distance as a heuristic
# it is registered as a solver with the name 'astar_ec'
class ASTAR_Euclidean(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.sqrt((cy - gy) ** 2 + (cx - gx) ** 2)


# this is the ASTAR variant with the manhattan distance as a heuristic
# it is registered as a solver with the name 'astar_mh'
class ASTAR_Manhattan(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.fabs((cy - gy)) + math.fabs(cx - gx)
