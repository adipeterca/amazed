from amazed.maze import Maze
from amazed.solver.Solver import Solver
import numpy as np

class CostCell:
    def __init__(self, x, y, distance, visited):
        self.x = x
        self.y = y
        self.distance = distance
        self.visited = visited

    def visit(self):
        self.visited = True

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y
    
    def to_tuple(self):
        return (self.x, self.y)

class Dijstra(Solver):
    def __init__(self, maze: Maze, start=None, end=None):
        '''
        If the @end node is not set, it will compute the distance to all nodes.
        '''
        self.maze = maze
        self.steps = []
        self.visited = []

        self.start = (0, 0) if start is None else start
        self.end = end

    def solve(self, cost_matrix:np.ndarray):
        '''
        Applies Dijstra traversal algorithm using the provided @cost_matrix.\n
        If all values are equal to 1, then it is the same as Lee's.
        '''

        '''
        
        Problema trebuie pusa cu costuri pe ZIDURI, nu pe celule, pt ca daca [X, Y] = 1 si [X,Y+1] = 10, 
        cum calculez distanta? adun +1 sau +10? Daca adun celula curenta, atunci mergand de la [X,Y] la [X,Y+1] am +1,
        dar mergand de la [X,Y+1] la [X,Y] am +10.
        
        '''

        # if cost_matrix.shape[0] != self.maze.rows:
        #     raise ValueError(f"@cost_matrix shape 0 '{cost_matrix.shape[0]}' does not match number of rows {self.maze.rows}.")
        # if cost_matrix.shape[1] != self.maze.columns:
        #     raise ValueError(f"@cost_matrix shape 1 '{cost_matrix.shape[1]}' does not match number of columns {self.maze.columns}.")
        
        # cells = []
        # for i in range(self.maze.rows):
        #     for j in range(self.maze.columns):
        #         if self.start == (i, j):
        #             cells.append(CostCell(i, j, 0, False))
        #         else:
        #             cells.append(CostCell(i, j, np.inf, False))

        # while True:
        #     # Select the unvisited cell with the smallest distance
        #     curr_cell = None
        #     for cell in cells:
        #         if not cell.visited:
        #             if curr_cell is None or curr_cell.distance > cell.distance:
        #                 curr_cell = cell
            
        #     if curr_cell is None:
        #         break

        #     if self.end is not None and curr_cell.to_tuple() == self.end:
        #         print(f"Found a path from {self.start} to {self.end} which costs {curr_cell.distance}.")
        #         break


        # # while there are unvisited cells and they are reachable
        # while len(unvisited_set) != 0 and unvisited_set[0][2] != np.inf:
        #     x, y, dist = unvisited_set.pop(0)
        #     visited_set.append((x, y))
            
        #     if self.end is not None and (x, y) == self.end:
        #         print(f"Found a path from {self.start} to {self.end} which costs {dist}.")
        #         break

        #     # Update path to unvisited neighbors
        #     if self.maze.is_valid_position(x-1, y) and not (x-1, y) in visited_set:

        #         old_dist = distances[(x-1, y)]
        #         new_dist = dist

                
