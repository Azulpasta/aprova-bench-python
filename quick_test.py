#!/usr/bin/env python3

from dominoes import can_chain

# Test the three element case
dominoes = [(1, 2), (3, 1), (2, 3)]
result = can_chain(dominoes)
print(f"Input: {dominoes}")
print(f"Output: {result}")

if result:
    # Verify the chain
    print("\nValidation:")
    print(f"  First number: {result[0][0]}")
    print(f"  Last number: {result[-1][1]}")
    print(f"  Match: {result[0][0] == result[-1][1]}")

    # Check consecutive dominoes match
    for i in range(len(result) - 1):
        print(f"  {result[i]}[1] == {result[i+1]}[0]: {result[i][1]} == {result[i+1][0]} = {result[i][1] == result[i+1][0]}")

# Test a case that should fail
print("\n" + "="*50)
print("Testing invalid case:")
dominoes2 = [(1, 2), (4, 1), (2, 3)]
result2 = can_chain(dominoes2)
print(f"Input: {dominoes2}")
print(f"Output: {result2}")
print(f"Expected: None (degrees not all even)")
