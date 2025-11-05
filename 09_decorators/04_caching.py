def cache_results(func):
    # The cache dictionary is stored in the decorator's closure scope.
    cache = {}

    def wrapper(a, b):
        # Create an immutable key from the arguments.
        # This works because the decorated function 'multiply' takes two simple arguments.
        key = (a, b)
        
        # Check if the result is already in the cache
        if key in cache:
            # Return the cached result with the "From Cache" message
            return f"From Cache: {cache[key]}"
        else:
            # Compute the result by calling the original function
            result = func(a, b)
            
            # Cache the new result
            cache[key] = result
            
            # Return the newly computed result with the "Computed" message
            return f"Computed: {result}"

    return wrapper

@cache_results
def multiply(a: int, b: int) -> int:
    # This is the heavy calculation (simulated here by a simple multiplication)
    return a * b

# --- Demonstration ---

# 1. First call (New computation)
print(f"Call 1: {multiply(5, 10)}")

# 2. Second call (New computation)
print(f"Call 2: {multiply(3, 4)}")

# 3. Third call (Repeated arguments - From Cache)
print(f"Call 3: {multiply(5, 10)}")

# 4. Fourth call (Repeated arguments - From Cache)
print(f"Call 4: {multiply(3, 4)}")

# 5. Fifth call (New computation)
print(f"Call 5: {multiply(1, 100)}")