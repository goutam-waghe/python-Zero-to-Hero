import copy

my_list = [10, 20, 30, 40]
print(my_list)  

fruits = ['apple', 'banana', 'cherry']

print(fruits[1])      # Output: banana
fruits[1] = 'mango'   # banana -> mango
print(fruits)    

# methods 

# append 

fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']


# insert

fruits.insert(1, 'mango')
print(fruits)  # ['apple', 'mango', 'banana', 'cherry']

# remove
fruits.remove('banana')
print(fruits)  # ['apple', 'mango', 'cherry']

# pop
fruits.pop()
print(fruits)  # ['apple', 'mango']

# pop
fruits.pop(0)
print(fruits)  # ['mango']

# sort

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # [1, 2, 5, 9]

# reverse

numbers.reverse()
print(numbers)  # [9, 5, 2, 1]

nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # Output: 3

# add two list 
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # Output: [1, 2, 3, 4]

# also 
original = [1,[ 2 , 4], 3]
copy_list = original.copy()
copy_list[2] = 7
print(copy_list)  # [1, 2, 3]
print(original)


#deep copy and shellow copy

# shellow: Shallow copy outer list ka naya object banata hai, lekin andar jo inner lists hoti hain, unki reference (link) hi copy karta hai — naye objects nahi banata.
original = [1,[ 2 , 4], 3]
copy_list = original.copy()
copy_list[2] = 7
print(copy_list)  # [1, 2, 3]
print(original)

# deepcopy : Deep copy outer list ke saath-saath andar ki har nested object (inner list) ka completely naya copy banata hai.

original = [1,[ 2 , 4], 3]
copy_list = original.c()
copy_list[2] = 7
print(copy_list)  # [1, 2, 3]
print(original)




