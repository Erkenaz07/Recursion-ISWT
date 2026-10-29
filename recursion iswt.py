def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)


def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + array_sum(arr[1:])


def find_max(arr):
    if len(arr) == 0:
        raise ValueError("The array cannot be empty")
    if len(arr) == 1:
        return arr[0]
    max_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_rest else max_rest


def count_occurrences(arr, x):
    if len(arr) == 0:
        return 0
    return (1 if arr[0] == x else 0) + count_occurrences(arr[1:], x)


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    if arr[middle] == target:
        return middle
    if target < arr[middle]:
        return binary_search(arr, target, left, middle - 1)
    return binary_search(arr, target, middle + 1, right)


def hanoi(n, source, helper, target):
    if n == 0:
        return
    hanoi(n - 1, source, target, helper)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, helper, source, target)


def subsets(arr, index=0, current=None):
    if current is None:
        current = []
    if index == len(arr):
        print(current)
        return
    subsets(arr, index + 1, current)
    subsets(arr, index + 1, current + [arr[index]])


def permutations(text, prefix=""):
    if len(text) == 0:
        print(prefix)
        return
    for i in range(len(text)):
        permutations(text[:i] + text[i + 1:], prefix + text[i])


def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    path = []
    visited = set()

    def go(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 1 or (r, c) in visited:
            return False
        path.append((r, c))
        if (r, c) == (rows - 1, cols - 1):
            return True
        visited.add((r, c))
        if go(r + 1, c) or go(r, c + 1) or go(r - 1, c) or go(r, c - 1):
            return True
        path.pop()
        return False

    if go(0, 0):
        return path
    return None


def n_queens(n):
    solutions = []
    board = [-1] * n

    def place(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            safe = True
            for old_row in range(row):
                if board[old_row] == col or abs(board[old_row] - col) == abs(old_row - row):
                    safe = False
                    break
            if safe:
                board[row] = col
                place(row + 1)
                board[row] = -1

    place(0)
    return solutions


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")


def main():
    print("1. Factorial:", factorial(5))
    print("2. Sum of numbers:", sum_numbers(5))
    print("3. Power:", power(2, 5))
    print("4. Count digits:", count_digits(58321))
    print("5. Sum of digits:", sum_digits(58321))
    print("6. Reverse number:", reverse_number(12345))
    print("7. Fibonacci:", fibonacci(7))
    print("   Time complexity: O(2^n) for this simple recursive version")
    print("8. GCD:", gcd(48, 18))
    print("9. Array sum:", array_sum([2, 4, 6, 8]))
    print("10. Maximum:", find_max([4, 8, 2, 15, 7]))
    print("11. Occurrences:", count_occurrences([2, 5, 2, 8, 2, 9], 2))
    print("12. Palindrome 'level':", is_palindrome("level"))
    print("13. Reverse string:", reverse_string("algorithm"))
    print("14. Binary search index:", binary_search([2, 4, 7, 10, 15, 21], 15))
    print("    Time complexity: O(log n)")
    print("15. Tower of Hanoi for n = 3:")
    hanoi(3, "A", "B", "C")
    print("16. Subsets of [1, 2, 3]:")
    subsets([1, 2, 3])
    print("17. Permutations of ABC:")
    permutations("ABC")
    print("18. Maze path:")
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    print(solve_maze(maze))
    print("19. N-Queens solutions for N = 4:")
    for solution in n_queens(4):
        print(solution)
    print("20. Binary tree traversals:")
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(20)
    print("Preorder:", end=" ")
    preorder(root)
    print()
    print("Inorder:", end=" ")
    inorder(root)
    print()
    print("Postorder:", end=" ")
    postorder(root)
    print()


if __name__ == "__main__":
    main()
