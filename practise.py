set1={1,2,3,4,5}
set2={1,2,3,6,7}
print("set1 :",set1)
print("Set2 :", set2)
print("uniun of set 1&2 :",set1.union(set2))
print("intersection of set 1&2 :",set1.intersection(set2))
print("set1-set2 :",set1.difference(set2))
print("set2-set1 :",set2.difference(set1))
print("is set2 subset of set1 :",set2.issubset(set1))
print("is set1 subset of set2 :",set1.issubset(set2))