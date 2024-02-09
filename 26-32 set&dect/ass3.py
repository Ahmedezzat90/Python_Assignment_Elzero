# print set , clear it , print it , add two elements , print it and delete c(not exist) element and print it without error

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}

print(my_set)

my_set.clear()
print(my_set)

my_set.add("B")
my_set.add("A")
print(my_set)

my_set.discard("C")
print(my_set)
