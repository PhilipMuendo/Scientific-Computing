def classify_number(number):
    """Classifies a number as even or odd."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    """Main function to execute the control structure challenges."""

    #Check even or odd
    try:
        user_input = int(input("Enter an integer: "))
        classification = classify_number(user_input)
        print(f"The number {user_input} is {classification}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    #Generate even number list
    even_numbers = []
    for i in range(2, 51, 2):  
        even_numbers.append(i)
    print("Even numbers from 1 to 50:", even_numbers)

    #Print numbers in reverse order
    count = 10
    while count >= 1:
        print(count)
        count -= 1

if __name__ == "__main__":
    main()