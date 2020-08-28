# number_list = [1, 3, 5, 7, 9]
# for i in number_list:
#   print(i+1)


#   #  2, 4, 6, 8, 10 is printed. 


# my_list = ['h', 'e', 'l', 'l', 'o']
# for i in range(len(my_list)):
#     print(i)


# x = list(range(100))
# for i in x:
#     print(i ** 2)

# x = [list(range(5)), list(range(5,11))]
# for i in x:
#     print(i)

"""In the code cell below, use list iteration to accomplish the following:

    In a list called even_nums append all the even numbers from the original list, iteration_list
    Similarly, in a variable called even_idx, collect all the values which are associated with the even indices in the original list, iteration_list

"""
iteration_list = list(range(1, 1000, 3))

# print(iteration_list)

even_nums = []

even_idx = []

for element in iteration_list:
  if element%2 == 0:
    even_nums.append(element)

for i, element in enumerate(iteration_list): 
  if i%2 == 0: 
    even_idx.append(element)


    
print (even_nums)
print (even_idx)