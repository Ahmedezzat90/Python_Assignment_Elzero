# This code creates two variables, num_one and num_two, and assigns them the values 10 and 20, respectively. It then adds the two variables together and stores the result in a new variable called result, which is printed on the first line. On the second line, it calculates the result of raising the number to the power of 3. On the third line, it calculates the remainder of the number divided by 26000. On the fourth line, it prints the result of dividing the number by 5. It then prints the type of the result after converting it to a string to ensure that it is a string.
num_one = 10
num_two = 20

result = num_one + num_two 
print(result)

result = result ** 3 
print(result)

result = result % 26000 
print(result)

result = float(result) / 5 
print(result)

print(type(str(result)))