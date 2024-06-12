import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None, depth=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return (self.depth + self.manhattan()) < (other.depth + other.manhattan())

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != 0:
                    target_row, target_col = divmod(self.puzzle[i][j] - 1, 3)
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance

    def is_goal(self):
        return self.manhattan() == 0

    def get_neighbors(self):
        neighbors = []
        zero_row, zero_col = next((i, j) for i, row in enumerate(self.puzzle) for j, val in enumerate(row) if val == 0)

        for i, j in [(zero_row - 1, zero_col), (zero_row + 1, zero_col), (zero_row, zero_col - 1), (zero_row, zero_col + 1)]:
            if 0 <= i < 3 and 0 <= j < 3:
                neighbor_puzzle = [row[:] for row in self.puzzle]
                neighbor_puzzle[zero_row][zero_col], neighbor_puzzle[i][j] = neighbor_puzzle[i][j], neighbor_puzzle[zero_row][zero_col]
                neighbors.append(PuzzleState(neighbor_puzzle, parent=self, move=(i, j), depth=self.depth + 1))
        return neighbors

def solve_puzzle(initial_state):
    heap = [initial_state]
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        visited.add(current_state)
        for neighbor in current_state.get_neighbors():
            if neighbor not in visited:
                heapq.heappush(heap, neighbor)

    return None

def get_user_input():
    print("Enter the initial state of the 8-puzzle (0 represents the empty space):")
    initial_puzzle = []
    for i in range(3):
        row = list(map(int, input().split()))
        initial_puzzle.append(row)
    return initial_puzzle

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    initial_puzzle = get_user_input()
    initial_state = PuzzleState(initial_puzzle)
    solution_path = solve_puzzle(initial_state)

    if solution_path:
        for step, puzzle_state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_puzzle(puzzle_state.puzzle)
            print()
    else:
        print("No solution found.")
