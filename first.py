import random as ran
def fun(length):
    calpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # capital alphabet
    salpha="abcdefghijklmnopqrstuvwxyz"  # small alphabet
    num="0123456789"
    sc="@#$&"
    st=calpha+salpha+num+sc
    st1=""
    while len(st1) !=length:
            st1+=ran.choice(st)
    return st1
leg=input("enter length of password") 
print(fun(int(leg)))

