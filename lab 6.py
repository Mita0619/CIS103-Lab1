#Problem 1: Basic Arithmetic and Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#Problem 2: Temperature Converter
def convert_temperature(temp, unit):
    if unit.upper() == 'C':
        return (temp * 9 / 5) + 32  # Convert Celsius to Fahrenheit
    elif unit.upper() == 'F':
        return (temp - 32) * 5 / 9  # Convert Fahrenheit to Celsius
    else:
        return "Invalid unit. Please use 'C' or 'F'."
print(convert_temperature(32, 'F'))
print(convert_temperature(0, 'C'))
print(convert_temperature(100, 'C'))

#Problem 3: List Manipulation
def analyze_numbers():
    numbers_str = input("Enter a list of numbers separated by commas: ")
    numbers_list = [int(num) for num in numbers_str.split(",")]
    maximum = max(numbers_list)
    minimum = min(numbers_list)
    total_sum = sum(numbers_list)
    sorted_list = sorted(numbers_list)
    print(f"Maximum number: {maximum}")
    print(f"Minimum number: {minimum}")
    print(f"Sum of numbers: {total_sum}")
    print(f"Sorted list: {sorted_list}")
if __name__ == "__main__":
    analyze_numbers()

#Problem 4: String Reversal
def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))


#Problem 5: Factorial Calculation
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
print(calculate_factorial(5))
print(calculate_factorial(0))
print(calculate_factorial(-3))


#Problem 6: Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))
print(is_prime(2))
print(is_prime(1))

#Problem 7: Dictionary of Word Frequencies
def word_frequency(sentence):
    word_dict = {}
    words = sentence.lower().split()  # Split sentence into words, convert to lowercase
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
user_sentence = input("Enter a sentence: ")
word_freq = word_frequency(user_sentence)
print(word_freq)