from typing import List, Optional, Tuple


def load_trees() -> List[List[int]]:
    with open("data/day8.txt", "r") as file:
        trees = file.read().split("\n")

    return [list(map(lambda x: int(x), tree)) for tree in trees]


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    height = len(matrix)
    width = len(matrix[0])
    result = [[0 for _ in range(height)] for _ in range(width)]

    for i in range(width):
        for j in range(height):
            result[i][j] = matrix[j][i]

    return result


def is_visible(point: int, first_neighbor: Optional[List[int]] = None, second_neighbor: Optional[List[int]] = None) -> bool:
    if not first_neighbor:
        return True

    if not second_neighbor:
        return True

    first_neighbor_max = max(first_neighbor)
    second_neighbor_max = max(second_neighbor)

    if point > first_neighbor_max or point > second_neighbor_max:
        return True

    return False


def get_scenic_index(point: int, neighbor: List[int]) -> int:
    scenic_index = 0

    for idx, val in enumerate(neighbor):
        scenic_index += 1

        if point <= val:
            break

    return scenic_index


def get_scenic_score(point: int, first_neighbor: Optional[List[int]] = None, second_neighbor: Optional[List[int]] = None) -> int:
    if not first_neighbor:
        return 0

    if not second_neighbor:
        return 0

    first_scenic_index = get_scenic_index(point, first_neighbor[::-1])
    second_scenic_index = get_scenic_index(point, second_neighbor)

    return first_scenic_index * second_scenic_index


def get_solutions(trees: List[List[int]]) -> Tuple[int, int]:
    transposed_trees = transpose_matrix(trees)

    total = 0
    scenic_scores = []
    height = len(trees)
    width = len(trees[0])

    for row in range(height):
        for col in range(width):
            # solve the first question, using is_visible helper method
            left_right_visible = is_visible(trees[row][col], trees[row][0:col], trees[row][col + 1 : width])
            top_bottom_visible = is_visible(
                transposed_trees[col][row], transposed_trees[col][0:row], transposed_trees[col][row + 1 : height]
            )
            total += left_right_visible or top_bottom_visible
            # solve the second question, using get_scenic_score helper method
            left_right_score = get_scenic_score(trees[row][col], trees[row][0:col], trees[row][col + 1 : width])
            top_bottom_score = get_scenic_score(
                transposed_trees[col][row], transposed_trees[col][0:row], transposed_trees[col][row + 1 : height]
            )
            scenic_scores.append(left_right_score * top_bottom_score)

    return total, max(scenic_scores)


ans_1, ans_2 = get_solutions(load_trees())
print(f"Solution 1: {ans_1}")
print(f"Solution 2: {ans_2}")
