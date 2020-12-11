# list comprehension
list=[1,2,3,4,5,6,7,8]
even_num_list=[]
for num in list:
    if num%2==0:
         even_num_list.append(num)
print("even number :",even_num_list)

even_num_list=[num for num in list if num%2==0]

print(even_num_list)