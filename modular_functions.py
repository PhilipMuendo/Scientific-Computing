import math

def calculate_area(shape, dimension1, dimension2=0):
    """Calculates the area of a given shape."""
    shape = shape.lower()  # Make shape case-insensitive

    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

def main():
    """Tests the calculate_area function with different shapes."""

    # Test cases
    print("Area of circle (radius 5):", calculate_area("circle", 5))
    print("Area of rectangle (length 4, width 6):", calculate_area("rectangle", 4, 6))
    print("Area of triangle (base 8, height 3):", calculate_area("triangle", 8, 3))
    print("Area of invalid shape:", calculate_area("square", 5, 5)) #test for an invalid shape.
    print("Area of rectangle (length 7, width 0):",calculate_area("rectangle",7)) #test rectangle with a single dimension.

if __name__ == "__main__":
    main()