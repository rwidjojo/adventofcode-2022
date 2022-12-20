from typing import Optional, List

def load_trees():
    with open("data/day8.txt", "r") as file:
        trees = file.read().split("\n")

    return [list(map(lambda x: int(x), tree)) for tree in trees]


def is_visible(point: int, first_neighbor: Optional[List[int]] = None, second_neighbor: Optional[List[int]] = None):
    if not first_neighbor:
        return True
    
    if not second_neighbor:
        return True

    first_neighbor_max = max(first_neighbor)
    second_neighbor_max = max(second_neighbor)
    
    if point > first_neighbor_max or point > second_neighbor_max:
        return True

    return False


def transpose_matrix(matrix: List[List[int]]):
    height = len(matrix)
    width = len(matrix[0])
    result = [[0 for _ in range(height)] for _ in range(width)]

    for i in range(width):
        for j in range(height):
            result[i][j] = matrix[j][i]

    return result


def get_visible_count(trees: List[List[int]]):
    transposed_trees = transpose_matrix(trees)
    
    total = 0
    height = len(trees)
    width = len(trees[0])

    for row in range(height):
        for col in range(width):
            left_right_visible = is_visible(trees[row][col], trees[row][0:col], trees[row][col+1:width])
            top_bottom_visible = is_visible(transposed_trees[col][row], transposed_trees[col][0:row], transposed_trees[col][row+1:height])
            total += left_right_visible or top_bottom_visible

    return total

print(f"Solution 1: {get_visible_count(load_trees())}")
print(f"Solution 2: ")
