#!/usr/bin/env python3

from dominoes import can_chain

def test_basic_cases():
    # Test 1: Empty input
    result = can_chain([])
    print(f"Empty: {result}")
    assert result == [], f"Expected [], got {result}"

    # Test 2: Singleton that works
    result = can_chain([(1, 1)])
    print(f"Singleton (1,1): {result}")
    assert result is not None, "Should have a chain"
    assert result[0][0] == result[0][1], "Should form a valid chain"

    # Test 3: Singleton that doesn't work
    result = can_chain([(1, 2)])
    print(f"Singleton (1,2): {result}")
    assert result is None, "Should not have a chain (1 != 2)"

    # Test 4: Three elements
    result = can_chain([(1, 2), (3, 1), (2, 3)])
    print(f"Three elements: {result}")
    assert result is not None, "Should have a chain"
    # Verify it's a valid chain
    assert result[0][0] == result[-1][1], "First and last must match"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], f"Chain broken between {result[i]} and {result[i+1]}"

    # Test 5: Can't be chained
    result = can_chain([(1, 2), (4, 1), (2, 3)])
    print(f"Can't chain (1,2), (4,1), (2,3): {result}")
    assert result is None, "Should not have a chain"

    # Test 6: Disconnected simple
    result = can_chain([(1, 1), (2, 2)])
    print(f"Disconnected (1,1), (2,2): {result}")
    assert result is None, "Should not have a chain (disconnected)"

    print("\nAll basic tests passed!")

if __name__ == '__main__':
    test_basic_cases()
