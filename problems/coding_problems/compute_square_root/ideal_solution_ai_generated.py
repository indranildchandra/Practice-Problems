"""
Square Root Implementation Without Using Built-in Functions

This module demonstrates different approaches to calculate square root
without using math.sqrt() or ** 0.5 operators.
"""


def square_root_newton(n, tolerance=1e-10):
    """
    Calculate square root using Newton's Method (Newton-Raphson).
    
    Formula: x_new = (x_old + n/x_old) / 2
    
    This is the most efficient method with quadratic convergence.
    
    Args:
        n: Number to find square root of
        tolerance: Precision level (default: 1e-10)
    
    Returns:
        Square root of n
    
    Time Complexity: O(log n)
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0
    
    # Initial guess
    x = n
    
    # Iterate until convergence
    while True:
        # Newton's formula: x_new = (x + n/x) / 2
        x_new = (x + n / x) / 2
        
        # Check if we've converged
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new


def square_root_binary_search(n, tolerance=1e-10):
    """
    Calculate square root using Binary Search method.
    
    This method searches for the square root in the range [0, n].
    
    Args:
        n: Number to find square root of
        tolerance: Precision level (default: 1e-10)
    
    Returns:
        Square root of n
    
    Time Complexity: O(log n)
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Set the search boundaries
    if n < 1:
        left, right = n, 1
    else:
        left, right = 0, n
    
    # Binary search
    while right - left > tolerance:
        mid = (left + right) / 2
        square = mid * mid
        
        if abs(square - n) < tolerance:
            return mid
        elif square < n:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2


def square_root_babylonian(n, max_iterations=100):
    """
    Calculate square root using Babylonian Method (ancient method).
    
    This is essentially the same as Newton's method but with a different
    perspective - it's the average of the number and its estimate.
    
    Args:
        n: Number to find square root of
        max_iterations: Maximum number of iterations (default: 100)
    
    Returns:
        Square root of n
    
    Time Complexity: O(log n)
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0
    
    # Start with n as initial guess
    guess = n
    
    for _ in range(max_iterations):
        # Better guess is the average of current guess and n/guess
        better_guess = (guess + n / guess) / 2
        
        # If the difference is negligible, we've found our answer
        if abs(better_guess - guess) < 1e-10:
            return better_guess
        
        guess = better_guess
    
    return guess


def square_root_digit_by_digit(n):
    """
    Calculate square root using digit-by-digit algorithm.
    
    This is similar to long division and works well for perfect squares.
    
    Args:
        n: Number to find square root of (integer)
    
    Returns:
        Integer square root of n
    
    Time Complexity: O(log n)
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0
    
    # For integer square root
    result = 0
    bit = 1 << ((n.bit_length() + 1) // 2)
    
    while bit != 0:
        if (result + bit) * (result + bit) <= n:
            result += bit
        bit >>= 1
    
    return result


# Demo and testing
if __name__ == "__main__":
    import time
    
    # Test numbers
    test_numbers = [4, 16, 25, 100, 144, 2, 3, 0.5, 1000, 123456]
    
    print("=" * 80)
    print("SQUARE ROOT CALCULATION WITHOUT BUILT-IN FUNCTIONS")
    print("=" * 80)
    print()
    
    for num in test_numbers:
        print(f"\nFinding square root of {num}:")
        print("-" * 60)
        
        # Method 1: Newton's Method
        start = time.perf_counter()
        result_newton = square_root_newton(num)
        time_newton = time.perf_counter() - start
        print(f"Newton's Method:        {result_newton:.10f} (Time: {time_newton*1e6:.2f} µs)")
        
        # Method 2: Binary Search
        start = time.perf_counter()
        result_binary = square_root_binary_search(num)
        time_binary = time.perf_counter() - start
        print(f"Binary Search:          {result_binary:.10f} (Time: {time_binary*1e6:.2f} µs)")
        
        # Method 3: Babylonian Method
        start = time.perf_counter()
        result_babylonian = square_root_babylonian(num)
        time_babylonian = time.perf_counter() - start
        print(f"Babylonian Method:      {result_babylonian:.10f} (Time: {time_babylonian*1e6:.2f} µs)")
        
        # For integers, show digit-by-digit method
        if isinstance(num, int) or num == int(num):
            result_digit = square_root_digit_by_digit(int(num))
            print(f"Digit-by-Digit (int):   {result_digit}")
        
        # Verify with built-in (for comparison only)
        actual = num ** 0.5
        print(f"Verification (x**0.5):  {actual:.10f}")
        
        # Check accuracy
        error_newton = abs(result_newton - actual)
        print(f"Newton's Error:         {error_newton:.2e}")
    
    print("\n" + "=" * 80)
    print("SPECIAL CASES")
    print("=" * 80)
    
    # Test edge cases
    print("\nEdge Cases:")
    print(f"sqrt(0) = {square_root_newton(0)}")
    print(f"sqrt(1) = {square_root_newton(1)}")
    print(f"sqrt(0.01) = {square_root_newton(0.01)}")
    
    # Test error handling
    print("\nError Handling:")
    try:
        square_root_newton(-1)
    except ValueError as e:
        print(f"sqrt(-1) raises ValueError: {e}")
    
    print("\n" + "=" * 80)
    print("\nRECOMMENDATION:")
    print("Newton's Method is the most efficient and accurate for most use cases.")
    print("=" * 80)

