'''array =[1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0
for element in range array:
    if(element%2==0):
        even +=1
    else:
        odd +=1
print("even no = ",even)
print("odd no = ",odd)'''

# Create an array of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize the even and odd counters
even_count = 0
odd_count = 0

# Iterate over the array and count the even and odd numbers
for number in numbers:
  if number % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

# Print the results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)