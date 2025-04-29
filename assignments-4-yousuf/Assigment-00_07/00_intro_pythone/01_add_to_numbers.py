def main():
    # Get user input
    num1 = input("Enter the first number: ")
    num1 = int(num1)  # Convert to integer
    
    num2 = input("Enter the second number: ")
    num2 = int(num2)  # Convert to integer

    # Calculate the sum
    total_sum = num1 + num2

    # Display the result
    print(f"The sum of the two numbers is: {total_sum}")
    
if __name__ == "__main__":
        main()