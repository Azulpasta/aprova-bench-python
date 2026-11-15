#!/usr/bin/env python3
"""Final verification before running unit tests"""

from list_ops import (
    append, concat, foldl, foldr, length, reverse,
    filter as list_ops_filter,
    map as list_ops_map,
)

print("=" * 50)
print("TESTING ALL FUNCTIONS")
print("=" * 50)

# Test 1: append
print("\n1. Testing append:")
print(f"  append([], []) = {append([], [])} (expected [])")
print(f"  append([], [1,2,3,4]) = {append([], [1,2,3,4])} (expected [1,2,3,4])")
print(f"  append([1,2], [2,3,4,5]) = {append([1,2], [2,3,4,5])} (expected [1,2,2,3,4,5])")

# Test 2: concat
print("\n2. Testing concat:")
print(f"  concat([]) = {concat([])} (expected [])")
print(f"  concat([[1,2], [3], [], [4,5,6]]) = {concat([[1,2], [3], [], [4,5,6]])} (expected [1,2,3,4,5,6])")

# Test 3: length
print("\n3. Testing length:")
print(f"  length([]) = {length([])} (expected 0)")
print(f"  length([1,2,3,4]) = {length([1,2,3,4])} (expected 4)")

# Test 4: filter
print("\n4. Testing filter:")
print(f"  filter(lambda x: x%2==1, []) = {list_ops_filter(lambda x: x%2==1, [])} (expected [])")
print(f"  filter(lambda x: x%2==1, [1,2,3,5]) = {list_ops_filter(lambda x: x%2==1, [1,2,3,5])} (expected [1,3,5])")

# Test 5: map
print("\n5. Testing map:")
print(f"  map(lambda x: x+1, []) = {list_ops_map(lambda x: x+1, [])} (expected [])")
print(f"  map(lambda x: x+1, [1,3,5,7]) = {list_ops_map(lambda x: x+1, [1,3,5,7])} (expected [2,4,6,8])")

# Test 6: foldl
print("\n6. Testing foldl:")
result = foldl(lambda acc, el: el * acc, [], 2)
print(f"  foldl(lambda acc, el: el*acc, [], 2) = {result} (expected 2)")
result = foldl(lambda acc, el: el + acc, [1,2,3,4], 5)
print(f"  foldl(lambda acc, el: el+acc, [1,2,3,4], 5) = {result} (expected 15)")
result = foldl(lambda acc, el: el / acc, [1,2,3,4], 24)
print(f"  foldl(lambda acc, el: el/acc, [1,2,3,4], 24) = {result} (expected 64)")

# Test 7: foldr
print("\n7. Testing foldr:")
result = foldr(lambda acc, el: el * acc, [], 2)
print(f"  foldr(lambda acc, el: el*acc, [], 2) = {result} (expected 2)")
result = foldr(lambda acc, el: el + acc, [1,2,3,4], 5)
print(f"  foldr(lambda acc, el: el+acc, [1,2,3,4], 5) = {result} (expected 15)")
result = foldr(lambda acc, el: el / acc, [1,2,3,4], 24)
print(f"  foldr(lambda acc, el: el/acc, [1,2,3,4], 24) = {result} (expected 9)")
result = foldr(lambda acc, el: el + acc, ["e","x","e","r","c","i","s","m"], "!")
print(f"  foldr(lambda acc, el: el+acc, [...strings...], \"!\") = {result} (expected 'exercism!')")

# Test 8: reverse
print("\n8. Testing reverse:")
print(f"  reverse([]) = {reverse([])} (expected [])")
print(f"  reverse([1,3,5,7]) = {reverse([1,3,5,7])} (expected [7,5,3,1])")
print(f"  reverse([[1,2],[3],[],[4,5,6]]) = {reverse([[1,2],[3],[],[4,5,6]])} (expected [[4,5,6],[],[3],[1,2]])")

print("\n" + "=" * 50)
print("All manual checks completed!")
print("=" * 50)
