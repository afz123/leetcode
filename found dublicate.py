# Python3 code to demonstrate working of
# Duplicate element indices in list
# Using list comprehension + list slicing

# initializing list
test_list = [1, 4, 5, 5, 5, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# Duplicate element indices in list
# Using list comprehension + list slicing
res = [val for idx, val in enumerate(test_list) if val in test_list[:idx]]
		
# printing result
print("The list of duplicate elements is : " + str(res))




#_____________________________its more better

a=[0,0,1,1,1,2,2,3,3,4]
seen = set()
uniq = [x for x in a if x not in seen and not seen.add(x)]  
print(uniq)




for i,j in enumerate(test_list):
    print(i,j)