def analyze_value(value):
    """
    Analyze a value and return its characteristics.
    """
    value_type = type(value).__name__
    truthy = bool(value)

    if hasattr(value, "__len__"):
        try:
            length = len(value)
        except TypeError:
            length = "N/A"
    else:
        length = "N/A"

    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthy} | "
        f"Length: {length}"
    )


# Test cases
print(analyze_value(42))
print(analyze_value(""))
print(analyze_value([1, 2, 3]))