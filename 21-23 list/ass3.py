# in one line print all list elements except the first and last elements
# in two line print the first and last elements only


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
#               0        1        2       3        4
#               1        2        3       4        5
#               -5       -4       -3      -2       -1
# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"

print(friends[1:len(friends)-1])
print(f"['{friends[0]}', '{friends[-1]}']")


