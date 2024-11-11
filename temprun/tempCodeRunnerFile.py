
#///////////////////////////////////////////////////////////////////
# input_string = "this is great and Python is fun"

# words = input_string.split()
# result = ""

# for word in words:
#     if word not in result.lower().split():
#         result += word + " "
        
# print("Original String:", input_string)
# print("String without duplicates:", result)

#////////////////////////////////////////////////////////////////////

# # Input string
# input_string = "Hello@World!"

# # Define special characters
# special_characters = "!@#$%^&*()-+?_=,<>/"

# # Flag to check for special characters
# contains_special_char = False

# # Loop through each character in the input string
# for char in input_string:
#     # Loop through each special character
#     for special_char in special_characters:
#         # If the character is a special character, set the flag and break
#         if char == special_char:
#             contains_special_char = True
#             break
#     # Break the outer loop if a special character is found
#     if contains_special_char:
#         break

# # Display result
# if contains_special_char:
#     print("The string contains special characters.")
# else:
#     print("The string does not contain any special characters.")

#//////////////////////////////////////////////////////////////////////
    
# # Define a dictionary to map words to digits
# word_to_digit = {
#     "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
#     "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
# }

# # Input string
# input_string = "four zero one"

# # Split the input string into words
# words = input_string.split()

# # Initialize an empty result string
# result = ""

# # Loop through each word in the input string
# for word in words:
#     # Append the corresponding digit from the dictionary to the result
#     if word in word_to_digit:
#         result += word_to_digit[word]

# # Display the result
# print("Output:", result)

#/////////////////////////////////////////////////////

# Input string
# input_string = "hello world this is a test string"

# # Split the string into words
# words = input_string.split()

# # Sort the words in alphabetical order
# sorted_words = sorted(words)

# # Join the sorted words back into a single string
# result = ' '.join(sorted_words)

# # Display the result
# print("Original String:", input_string)
# print("Sorted String:", result)

#///////////////////////////////////////////////////////////////////////////

# import re

# text = "ThisIsAnExampleStringWithDifferentWords"

# # Double the backslashes because we're not using raw strings
# words = re.findall('[A-Z][a-z]*', text)

# # Join the list of words with spaces to form the final result
# result = " ".join(words)

# print(result)

#///////////////////////////////////////////////////////////////////////////
# import re

# def validate_name(name):
#  
#     pattern = r"^(Mr\.|Mrs\.|Ms\.)\s[A-Z][a-z]+(\s[A-Z][a-z]+)*$(\s[A-Z][a-z]+)*$"
    
#     
#     if re.match(pattern, name):
#         return True
#     else:
#         return False

# 
# names = [
#     "Mr. John Doe",            # Valid name
#     "Mrs. Jane Smith",         # Valid name
#     "Ms. Anna Marie Smith",    # Valid name with middle and last name
#     "Mr. john doe",            # Invalid name (first name starts with lowercase letter)
#     "Ms. John",                # Valid name (first name only)
#     "Mrs. John Smith Doe"      # Invalid name (last name after first name is optional)
# ]

# 
# for name in names:
#     if validate_name(name):
#         print(f"'{name}' is valid.")
#     else:
#         print(f"'{name}' is invalid.")

#////////////////////////////////////////////////////////////////////////////////////


# def sum_of_digits(number):
#     sum_digits = 0
   
#     while number > 0:
#         sum_digits += number % 10  
#         number = number // 10 
#     return sum_digits

# num = int(input("Enter a number: "))  
# result = sum_of_digits(num) 
# print("The sum of digits is:", result)  

#//////////////////////////////////////////////////////////////////////////

# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0

#     while number > 0:
#         last_digit = number % 10
#         reversed_number = (reversed_number * 10) + last_digit
#         number = number // 10

#     return original_number == reversed_number

# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")


#//////////////////////////////////////////////////////////////////////////////////

# def fibonacci_series(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for i in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence

# terms = int(input("Enter the number of terms: "))
# if terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci series:", fibonacci_series(terms))

#////////////////////////////////////////////////////////////////////////////////
 
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            content = src.read()
            dest.write(content)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source_file = 'source.txt'   
destination_file = 'destination.txt'  
copy_file(source_file, destination_file)

