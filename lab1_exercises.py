# ==========================================
# LAB 1: PYTHON FOUNDATIONS
# Advanced Python Course - Week 1
# ==========================================
# 
# INSTRUCTIONS:
# - Complete each exercise function below
# - Do not change function names or parameters
# - Test your code by running: python test_lab1.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# EXERCISE 1: Create Your Profile (5 points)
# ==========================================
def exercise1():
    """
    Create variables storing information about yourself and return them as a dictionary.
    
    Returns:
        dict: Dictionary with keys 'name', 'age', 'height', 'loves_programming'
    
    Example:
        {'name': 'John', 'age': 20, 'height': 1.75, 'loves_programming': True}
    """
    # TODO: Create four variables with your information
    your_name = ""  # Replace with your name
    your_age = 0
    your_height = 0.0
    loves_programming = False
    
    return {
        'name': your_name,
        'age': your_age,
        'height': your_height,
        'loves_programming': loves_programming
    }


# ==========================================
# EXERCISE 2: String Operations (5 points)
# ==========================================
def exercise2(first_name, last_name):
    """
    Combine first and last names with a space between.
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    
    Returns:
        str: Full name with space between
    
    Example:
        exercise2("John", "Doe") returns "John Doe"
    """
    # TODO: Combine first_name and last_name with a space
    full_name = ""
    
    return full_name


# ==========================================
# EXERCISE 3: Working with Numbers (5 points)
# ==========================================
def exercise3(test1, test2, test3):
    """
    Calculate the average of three test scores.
    
    Args:
        test1 (int): First test score
        test2 (int): Second test score
        test3 (int): Third test score
    
    Returns:
        float: Average of the three scores
    
    Example:
        exercise3(85, 92, 78) returns 85.0
    """
    # TODO: Calculate and return the average
    average = 0
    
    return average


# ==========================================
# EXERCISE 4: Temperature Converter (7 points)
# ==========================================
def exercise4(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    
    Example:
        exercise4(25) returns 77.0
    """
    # TODO: Calculate and return fahrenheit
    fahrenheit = 0
    
    return fahrenheit


# ==========================================
# EXERCISE 5: Rectangle Area (7 points)
# ==========================================
def exercise5(length, width):
    """
    Calculate the area and perimeter of a rectangle.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        dict: Dictionary with keys 'area' and 'perimeter'
    
    Example:
        exercise5(12.5, 8.3) returns {'area': 103.75, 'perimeter': 41.6}
    """
    # TODO: Calculate area and perimeter
    area = 0
    perimeter = 0
    
    return {'area': area, 'perimeter': perimeter}


# ==========================================
# EXERCISE 6: Shopping Cart (8 points)
# ==========================================
def exercise6(item_price, quantity, tax_rate):
    """
    Calculate shopping cart totals with tax.
    
    Args:
        item_price (float): Price per item
        quantity (int): Number of items
        tax_rate (float): Tax rate (e.g., 0.07 for 7%)
    
    Returns:
        dict: Dictionary with keys 'subtotal', 'tax', 'total'
    
    Example:
        exercise6(29.99, 4, 0.07) returns 
        {'subtotal': 119.96, 'tax': 8.3972, 'total': 128.3572}
    """
    # TODO: Calculate subtotal, tax, and total
    subtotal = 0
    tax = 0
    total = 0
    
    return {'subtotal': subtotal, 'tax': tax, 'total': total}


# ==========================================
# EXERCISE 7: Age Checker (8 points)
# ==========================================
def exercise7(age):
    """
    Check if someone can vote (18 or older).
    
    Args:
        age (int): Person's age
    
    Returns:
        str: "You can vote!" or "You cannot vote yet."
    
    Example:
        exercise7(16) returns "You cannot vote yet."
        exercise7(20) returns "You can vote!"
    """
    # TODO: Use if-else to check voting eligibility
    result = ""
    
    return result


# ==========================================
# EXERCISE 8: Grade Calculator (10 points)
# ==========================================
def exercise8(score):
    """
    Convert numerical score to letter grade.
    90+: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    
    Args:
        score (int): Numerical score
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    
    Example:
        exercise8(85) returns "B"
    """
    # TODO: Use if-elif-else to determine letter grade
    letter = ""
    
    return letter


# ==========================================
# EXERCISE 9: Discount Calculator (10 points)
# ==========================================
def exercise9(purchase_amount):
    """
    Calculate discount and final price.
    $100+: 20% off, $50-99: 10% off, <$50: no discount
    
    Args:
        purchase_amount (float): Original purchase amount
    
    Returns:
        dict: Dictionary with 'discount_rate', 'discount_amount', 'final_price'
    
    Example:
        exercise9(75) returns 
        {'discount_rate': 0.10, 'discount_amount': 7.5, 'final_price': 67.5}
    """
    # TODO: Determine discount rate based on purchase amount
    discount_rate = 0
    discount_amount = 0
    final_price = 0
    
    return {
        'discount_rate': discount_rate,
        'discount_amount': discount_amount,
        'final_price': final_price
    }


# ==========================================
# EXERCISE 10: Find and Fix Errors (8 points)
# ==========================================
def exercise10(radius):
    """
    Calculate the area of a circle.
    Formula: area = π × radius² (use 3.14159 for π)
    
    THIS CODE HAS ERRORS - FIX THEM!
    
    Args:
        radius (float): Radius of circle
    
    Returns:
        float: Area of circle
    
    Example:
        exercise10(5) returns 78.53975
    """
    # BUGGY CODE - FIX THE ERRORS:
    pi = 3.14159
    # TODO: Fix the errors in the calculation below
    area = Pi * Radius * Radius
    
    return area


# ==========================================
# EXERCISE 11: Logic Error (7 points)
# ==========================================
def exercise11(num):
    """
    Check if a number is positive, negative, or zero.
    
    THIS CODE HAS A LOGIC ERROR - FIX IT!
    
    Args:
        num (int): Number to check
    
    Returns:
        str: "positive", "negative", or "zero"
    
    Example:
        exercise11(5) returns "positive"
        exercise11(-3) returns "negative"
        exercise11(0) returns "zero"
    """
    # BUGGY CODE - FIX THE LOGIC:
    if num > 0:
        return "zero"  # Something is wrong here!
    elif num < 0:
        return "negative"
    else:
        return "positive"  # Something is wrong here too!


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab1.py' to test your solutions!")
