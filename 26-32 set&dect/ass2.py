# include the 2 set with 3 diffrent way to one set

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

# 1
nums.update(letters)
print(nums)

# 2
nums |= letters
print(nums)

# 3
nums = nums.union(letters)
print(nums)

