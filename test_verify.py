#!/usr/bin/env python3
"""Quick verification of implementations"""

from list_ops import (
    append, concat, foldl, foldr, length, reverse,
    filter as list_ops_filter,
    map as list_ops_map,
)

# Test append
assert append([], []) == []
assert append([], [1, 2, 3, 4]) == [1, 2, 3, 4]
assert append([1, 2], [2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]
print("✓ append tests pass")

# Test concat
assert concat([]) == []
assert concat([[1, 2], [3], [], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
print("✓ concat tests pass")

# Test filter
assert list_ops_filter(lambda x: x % 2 == 1, []) == []
assert list_ops_filter(lambda x: x % 2 == 1, [1, 2, 3, 5]) == [1, 3, 5]
print("✓ filter tests pass")

# Test length
assert length([]) == 0
assert length([1, 2, 3, 4]) == 4
print("✓ length tests pass")

# Test map
assert list_ops_map(lambda x: x + 1, []) == []
assert list_ops_map(lambda x: x + 1, [1, 3, 5, 7]) == [2, 4, 6, 8]
print("✓ map tests pass")

# Test foldl
assert foldl(lambda acc, el: el * acc, [], 2) == 2
assert foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5) == 15
result = foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24)
assert abs(result - 64) < 0.0001, f"Expected 64, got {result}"
print("✓ foldl tests pass")

# Test foldr
assert foldr(lambda acc, el: el * acc, [], 2) == 2
assert foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5) == 15
result = foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24)
assert abs(result - 9) < 0.0001, f"Expected 9, got {result}"
assert foldr(lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!") == "exercism!"
print("✓ foldr tests pass")

# Test reverse
assert reverse([]) == []
assert reverse([1, 3, 5, 7]) == [7, 5, 3, 1]
assert reverse([[1, 2], [3], [], [4, 5, 6]]) == [[4, 5, 6], [], [3], [1, 2]]
assert reverse(["xyz", 4.0, "cat", 1]) == [1, "cat", 4.0, "xyz"]
print("✓ reverse tests pass")

print("\n✅ All verification tests pass!")
