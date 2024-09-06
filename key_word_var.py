# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers in a given range
def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Example usage
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
print(f"Prime numbers between {start} and {end} are:")
print_primes(start, end)

#
for i in range(1, 11):
    print(i)


# final and except & added condition upper and lower
try:
    file = open('example.txt', 'r')
    content = file.read()
    #print(content)
    uppercase = content.upper()
    lowercase = content.lower()
    print(content.upper())
    print(content.lower())
    print("UpperCase:", uppercase)
    print("LowerCase:", lowercase)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")

#UpperCase & LowerCase
name = "RajesH"
uppercase = name.upper()
lowercase = name.lower()
print(name.upper())
print(name.lower())
print("UpperCase:", uppercase)
print("LowerCase:", lowercase)
