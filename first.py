import random as ran
def fun(length):
    print(type(length))
    calpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # capital alphabet
    salpha="abcdefghijklmnopqrstuvwxyz"  # small alphabet
    num="0123456789"
    sc="@#$&"
    st=calpha+salpha+num+sc
    st1="".join(ran.sample(st,length))
    return st1
leg=input("enter length of password") 
print(fun(int(leg)))