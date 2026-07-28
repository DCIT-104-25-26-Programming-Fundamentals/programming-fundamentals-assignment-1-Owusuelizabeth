# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — 
def calculate_sum(numbers):
  total = 0
  for num in numbers:
    total += num
    return total 
def calculate_average(numbers):
  if len(numbers) == 0:
    return 0.0
    return calculate_sum(numbers) / len(numbers)
 def calculate_max(numbers):
   if len(numbers) == 0:
     return None
     maximum = numbers[0]
     for num in numbers[1:]:
       if num > maximum: 
         maximum = num 
         return maximum
 def calculate_min(numbers):
   if len(numbers) == 0:
     return None 
     minimum = numbers[0]
     for num in numbers[1:]:
       if num < minimum:
         minimum = num 
         return minimum 
def main():
  try:
    count = int(input("How many numbers?"))
  except ValueError:
    print("Error: Input must be an integer.")
    return
 if count <= 0:
   print("Error: N must be a positive integer.")
   return
 numbers = []
for i in range(1, count + 1):
  num = float(input(f"Enter number {i}: "))
  numbers.append(num)
#Print results formatted to match expexted output format
total_sum = calculate_sum(numbers)
avg = calculate_average(numbers)
maximum = calculate_max(numbers)
minimum = calculate_min(numbers)

print("\nResults:")
print(f"Sum: {int(total_sum) if total_sum. is_integer() else total_sum}")
print(f"Average: {avg}")
print(f"Maximum: {int(maximum) if maximum.is_integer() else maximum}")
print(f"Minimum: {int(minimum) if minimum.is_integer() else minimum}")

if _name_=="_main_":
  main()
  

   
# =============================================================================

