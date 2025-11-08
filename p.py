def increment(number):
    """
    Increases the value of a number by 1.
    
    Args:
        number: The number to increment
        
    Returns:
        The number increased by 1
        number: A numeric value to increment
        
    Returns:
        The input number plus 1
    """
    return number + 1


if __name__ == "__main__":
    # Example usage
    value = 5
    result = increment(value)
    print(f"Original value: {value}")
    print(f"Incremented value: {result}")
    print(f"increment(5) = {increment(5)}")
    print(f"increment(0) = {increment(0)}")
    print(f"increment(-1) = {increment(-1)}")
