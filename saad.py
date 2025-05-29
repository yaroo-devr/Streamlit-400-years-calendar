# Basic Python Program

# 1. Variables and Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# 2. Conditional Statement
if age >= 18:
    print(f"Hello {name}, you are an adult.")
else:
    print(f"Hello {name}, you are a minor.")

# 3. Loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# 4. Function
def greet(user_name):
    return f"Nice to meet you, {user_name}!"

# 5. Function Call
message = greet(name)
print(message)
