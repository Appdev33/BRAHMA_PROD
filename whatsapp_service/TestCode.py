def max_min(ar, left, right):
    # Base case: If there's only one element
    if left == right:
        return ar[left], ar[left]
    
    # Find the middle index
    mid = (left + right) // 2
    
    # Recursively find the max and min in the left and right halves
    left_max, left_min = max_min(ar, left, mid)
    right_max, right_min = max_min(ar, mid + 1, right)
    
    # Combine the results from the left and right halves
    final_max = max(left_max, right_max)
    final_min = min(left_min, right_min)
    
    return final_max, final_min


def pow_dac(base, exp):
    # Base case: exponent is 0, return 1
    if exp == 0:
        return 1
    # Recurse, split into halves for efficient calculation
    half = pow_dac(base, exp // 2)
    
    result = half * half
    # If exponent is odd, multiply by base once more
    return result if exp % 2 == 0 else base * result

# Example usage
base = 2
exp = 10
result = pow_dac(base, exp)
print(f"{base}^{exp} = {result}")


# Example usage:
ar = [1, 2, 3, 4, 5, 6, 7, 8]
max_val, min_val = max_min(ar, 0, len(ar) - 1)
print(f"Max: {max_val}, Min: {min_val}")




