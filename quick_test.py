from list_ops import foldl, foldr

# Test foldl direction
result_foldl = foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24)
print(f"foldl test: {result_foldl} (expected 64)")

# Test foldr direction
result_foldr = foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24)
print(f"foldr test: {result_foldr} (expected 9)")

# String test
result_str = foldr(lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!")
print(f"foldr string: {result_str} (expected 'exercism!')")
