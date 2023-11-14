def is_solution_valid(mapping, words, result):
    num_words = len(words)
    num_result = len(result)
    num_values = []
    for word in words + [result]:
        num = 0
        for letter in word:
            num = num * 10 + mapping[letter]
        num_values.append(num)
    return sum(num_values[:-1]) == num_values[-1]
def solve_cryptarithmetic(words, result):
    letters = set(''.join(words) + result)
    if len(letters) > 10:
        return None
    from itertools import permutations
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if is_solution_valid(mapping, words, result):
            return mapping
    return None
words = ["send", "more"]
result = "money"
solution = solve_cryptarithmetic(words, result)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
