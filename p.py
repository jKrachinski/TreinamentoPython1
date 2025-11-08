def increment(number):
    """
    Increases the value of a number by 1.
    
    Args:
        number: The number to increment
        
    Returns:
        The number increased by 1
    """
    return number + 1


if __name__ == "__main__":
    # Example usage
    value = 5
    result = increment(value)
    print(f"Original value: {value}")
    print(f"Incremented value: {result}")
