"""
Problem Statement:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
 
You must not use any built-in exponent function or operator.


Logic Building:
- 9 --> 3 --> 3 * 3
- 16 --> 4 --> 4 * 4
- n --> m --> m * m = n

- n = 50,000
1 --> 1 * 1 = 1
100 --> 100 * 100 = 10000
	101 * 101 = 
	102 * 102 = 
	103 * 103 = 
1000 --> 1000 * 1000 = 10^6

x = 16
i = 1 : x/2 - 1 --> 1, 2, 3, 4, 5, 6, 7 --> middle point = 4

x = 25
i = 1 : x/2 - 1 --> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 --> middle point = 6 --> 36 > 25
                --> 1, 2, 3, 4, 5 --> middle point = 3 --> 9 < 25
                --> 4, 5 --> 


"""

def compute_square_root(x):
    if x == 0 or x == 1:
        return x
    
    start = 1 
    end = x//2
    result = 1

    while start <= end:
        # print(start, end)
        middle = (end + start) // 2
        sqr = middle * middle
        # print(middle, sqr)
        if sqr < x:
            result = middle # intermediate integer value (rounded down for non integer square root values)
            start = middle + 1
            # print("Updated start: ", start)
        elif sqr > x:
            end = middle - 1 
            # print("Updated end: ", end)
        else:
            # print("Nearest Square Root:", middle)
            return middle
    
    return result
    

# Test cases
if __name__ == "__main__":
    test_cases = [
        (4, 2),
        (8, 2),
        (9, 3),
        (16, 4),
        (25, 5),
        (50000, 223),
        (100, 10),
        (144, 12),
		(160, 12),
        (0, 0),
        (1, 1),
    ]
    
    print("=" * 60)
    print("Testing compute_square_root function:")
    print("=" * 60)
    
    for x, expected in test_cases:
        print(f"\nTest: sqrt({x})")
        result = compute_square_root(x)
        status = " -- PASS" if result == expected else " -- FAIL"
        print(f"{status}: Result = {result}, Expected = {expected}")
        print("-" * 60)
    
    print("=" * 60)
