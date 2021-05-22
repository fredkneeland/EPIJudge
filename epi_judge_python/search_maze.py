import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

class Node():
    def __init__(self, coord, parent):
        self.coord = coord
        self.children = []
        self.parent = parent

    def addChild(self, coord):
        self.children.append(coord)

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    newMaze = maze.copy()
    startNode = Node(s, None)
    endNode = None
    nodes = [startNode]

    x_len = len(maze)
    y_len = len(maze[0])

    x_vals = [-1, 1, 0, 0]
    y_vals = [0, 0, -1, 1]

    while len(nodes) > 0 and endNode == None:
        node = nodes.pop()

        for i in range(4):
            curr_x = node.coord.x+x_vals[i]
            curr_y = node.coord.y+y_vals[i]
            if curr_x < 0 or curr_x >= x_len or curr_y < 0 or curr_y >= y_len:
                continue

            if newMaze[curr_x][curr_y] == 0:
                new_coord = Coordinate(curr_x, curr_y)
                newMaze[curr_x][curr_y] = 1
                new_node = Node(new_coord, node)
                nodes.append(new_node)
                node.addChild(new_node)
                if curr_x == e.x and curr_y == e.y:
                    endNode = new_node
                    break

        if endNode != None:
            break

    if endNode != None:
        returnVal = [endNode.coord]

        curr_node = endNode.parent

        while curr_node.coord != startNode.coord:
            returnVal.insert(0, curr_node.coord)
            curr_node = curr_node.parent

        returnVal.insert(0, startNode.coord)
        return returnVal

    return []


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
