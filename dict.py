#dictonary 
# dict={key:value,.......}
dict={1:"bhopal",2:"indore",3:"ujjain",4:"sagar"}
dict[5]="dindori"
print(dict.items())
for key,value in dict.items():
    print(key,":", value)

# dict.popitem()  // delete with last in first out
# print(dict)
dict.pop(1) # delete with key    
