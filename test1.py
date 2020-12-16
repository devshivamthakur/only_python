list1=[1,2,3,4]
list2=["shivam","thakur","cool", "o1@"]
dict1=dict( zip(list1,list2))
list3=list(zip(list1,list2))
print(list3) #[(1, 'shivam'), (2, 'thakur'), (3, 'cool'), (4, 'o1@')]
# list1.pop(3) # list=[1,2,3]
# unzip zip : zip(*(listname))
tuple1,tuple2=zip(*list3)
print(tuple1,tuple1)
