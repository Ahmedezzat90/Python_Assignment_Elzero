# do list and do unique list include the unique num from the one list print the list and the type of the list(tran set to list) and remove the 5 from the list

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

uniqe_list = set(my_list)
print(uniqe_list)
print(type(list(uniqe_list)))

uniqe_list.remove(5)
print(uniqe_list)